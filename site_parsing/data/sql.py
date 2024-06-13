import sqlite3 

from datetime import date, datetime

class SqlEngine:
    
    filepath: str = r'./db/offers.db'
    
    def select(query: str, params: tuple = ()): 
        result = ()
        try:            
            sqliteConnection = sqlite3.connect(SqlEngine.filepath)
            cursor = sqliteConnection.cursor()
            
            cursor.execute(query, params)
            result = cursor.fetchall()
            
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
            
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                
        return result
    
    def insert(query: str, params: tuple = ()):
        try:
            sqliteConnection = sqlite3.connect(SqlEngine.filepath)
            cursor = sqliteConnection.cursor()
            
            cursor.execute(query, params)
            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
            
        finally:
            if sqliteConnection:
                sqliteConnection.close()

class BaseModel:
    table: str
    
    id: int
    
    @classmethod
    def get_attributes(cls):
        attrs = {}
        for t in cls.__mro__:
            if t == object or t == cls: continue
            if issubclass(t, BaseModel):
                attrs = t().get_attributes()
            
        for a, t in cls.__dict__["__annotations__"].items():
            attrs[a] = t
            
        if "table" in attrs:
            del attrs["table"]
            
        return attrs

    @classmethod
    def get_all(cls, filters: dict = {}):
        if cls == BaseModel:
            raise Exception("Cannot read SQL for class `BaseModel`")
        
        columns = cls.get_attributes().keys()
        table = cls.table
        query = f"""SELECT {', '.join(columns)} FROM {table}"""

        params = ()
        if filters:
            query += " WHERE "

            for key, values in filters.items():
                if key not in columns:
                    continue
                
                if not isinstance(values, tuple):
                    values = (values,)

                query += f"{key} IN ({', '.join(['?' for _ in values])}) AND "
                params += values
            
            query = query[:-5]
        
        result = SqlEngine.select(query, params)
        ret = []
        for e in result:
            obj = cls()
            for col, val in zip(columns, e):
                if val is None:
                    obj.__setattr__(col, val)
                elif cls.get_attributes()[col] == date and val is not None:
                    obj.__setattr__(col, datetime.strptime(val[:10], "%Y-%m-%d").date())
                elif cls.get_attributes()[col] == datetime and val is not None:
                    obj.__setattr__(col, datetime.strptime(val[:10], "%Y-%m-%d"))
                else:
                    obj.__setattr__(col, cls.get_attributes()[col](val))
                    
            ret.append(obj)
        return ret
    
    @classmethod
    def get_by_id(cls, id: int):
        if cls == BaseModel:
            raise Exception("Cannot read SQL for class `Base`")
        
        columns = (cls.get_attributes().keys())
        table = cls.table
        query = f""" SELECT {', '.join(columns)} FROM {table} WHERE id=?"""
        params = (id,)
        
        result = SqlEngine.select(query, params)[0]
        
        obj = cls()
        for col, val in zip(columns, result):
            if val is None:
                obj.__setattr__(col, val)
            elif cls.get_attributes()[col] == date and val is not None:
                obj.__setattr__(col, datetime.strptime(val[:10], "%Y-%m-%d").date())
            elif cls.get_attributes()[col] == datetime and val is not None:
                obj.__setattr__(col, datetime.strptime(val[:10], "%Y-%m-%d"))
            else:
                obj.__setattr__(col, cls.get_attributes()[col](val))
            
        return obj 
    
    @classmethod
    def add(cls, obj):
        if cls == BaseModel:
            raise Exception("Cannot read SQL for class `Base`")
        
        columns = tuple([key for key in cls.get_attributes().keys() if key != "id"])
        table = cls.table
        query = f""" INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in columns])})"""
        params = tuple([obj.__getattribute__(col) for col in columns])
        
        SqlEngine.insert(query, params)
    
    def __str__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v}' for k, v in self.__dict__.items()])})"
    
class SiteModel(BaseModel):  
    table: str = "api_site"  
    
    name: str
    url: str
    is_filtered: bool

class OfferModel(BaseModel):
    table: str = "api_offer"  
    
    site_id: int
    title: str
    description: str
    url: str
    date_publication: date
    location: str
    job_id: str
    offer_group_id: int
    
class OfferGroupModel(BaseModel):
    table: str = "api_offergroup"
    
    name: str
    
class FilterModel(BaseModel):
    table: str = "api_filter"
    
    offer_group_id: int
    key: str
    value: str