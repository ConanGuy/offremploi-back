from .sql import BaseModel, FilterModel, OfferGroupModel, OfferModel, SiteModel

from datetime import date

class Base:    
    classmodel = BaseModel
    
    id: int  
    
    def __init__(self, **kwargs) -> None:
        for key in self.__class__.get_attributes():
            self.__setattr__(key, kwargs.get(key, None))
    
    @classmethod
    def get_attributes(cls):
        attrs = {}
        for t in cls.__mro__:
            if t == object or t == cls: continue
            if issubclass(t, Base):
                attrs = t().get_attributes()
            
        for a, t in cls.__dict__["__annotations__"].items():
            attrs[a] = t
            
        if "table" in attrs:
            del attrs["table"]
            
        return attrs
    
    @classmethod
    def get_all(cls, filters: dict = {}):        
        return [cls.from_model(model) for model in cls.classmodel.get_all(filters)]
    @classmethod
    def get_by_id(cls, id: int):        
        return cls.from_model(cls.classmodel.get_by_id(id))  
    
    @classmethod
    def from_model(cls, model):
        if type(model) != cls.classmodel:
            raise Exception(f"Expected {cls.classmodel.__name__} instead of {type(model).__name__}")
        
        obj = cls()
        
        attrs = cls.get_attributes()
        for attr, modelAttr in zip(attrs.keys(), model.get_attributes()):
            if issubclass(attrs[attr], Base):
                submodel = attrs[attr].classmodel.get_by_id(model.__getattribute__(modelAttr))
                obj.__setattr__(attr, attrs[attr].from_model(submodel))
            else:
                obj.__setattr__(attr, model.__getattribute__(modelAttr))
        return obj
    
    def to_model(self):
        model = self.classmodel()
        
        attrs = self.get_attributes()
        for attr in attrs.keys():
            if issubclass(attrs[attr], Base):
                model.__setattr__(attr+"_id", self.__getattribute__(attr).id)
            else:
                model.__setattr__(attr, self.__getattribute__(attr))
        return model
    
    def add(self):
        self.classmodel.add(self.to_model())
        
    def __str__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v}' for k, v in self.__dict__.items()])})"
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Base):
            return False
        
        return all([self.__getattribute__(attr) == value.__getattribute__(attr) for attr in self.get_attributes() if attr != "id"])
    
class Site(Base):  
    classmodel = SiteModel
    
    name: str
    url: str
    is_filtered: bool
    
class OfferGroup(Base):
    classmodel = OfferGroupModel
    
    name: str

class Offer(Base):
    classmodel = OfferModel

    site: Site
    title: str
    description: str
    url: str
    date_publication: date
    location: str
    job_id: str
    offer_group: OfferGroup
    
    def exists(self) -> bool:
        existing_offers: list[Offer] = [offer for offer in Offer.get_all({"site_id": (self.site.id)})]
        attributes: list[str] = [attr for attr in Offer.get_attributes() if attr != "id"]
        
        for existing_offer in existing_offers:
            if self.job_id != None and self.job_id == existing_offer.job_id:
                return True
            
            if all([self.__getattribute__(attr) == existing_offer.__getattribute__(attr) for attr in attributes]):
                return True
        
        return False
    
class Filter(Base):
    classmodel = FilterModel
    
    offer_group: OfferGroup
    key: str
    value: str
    
def get_filters():    
    groups = {}
    for filter in Filter.get_all():
        if filter.offer_group.id not in groups:
            groups[filter.offer_group.id] = {}
        
        if filter.key not in groups[filter.offer_group.id]:
            groups[filter.offer_group.id][filter.key] = ()
        groups[filter.offer_group.id][filter.key] += (filter.value,)
        
    return groups

def test():
    print("Testing ORM")
    
    for offer in Offer.get_all():
        print(offer)
    
    print("End testing ORM")