from datetime import datetime
from models import storage
import uuid
import copy


class BaseModel:

  def __init__(self, *args, **kwargs):
    if not kwargs:
      self.id = str(uuid.uuid4())
      self.created_at = datetime.now()
      self.updated_at = datetime.now()
      storage.new(self)

    else:
      for key in list(kwargs):
        if key == "__class__":
          continue
        elif key == "id":
          self.id = kwargs.get(key)
        elif key == "created_at":
          self.created_at = datetime.fromisoformat(kwargs.get(key))
        elif key == "updated_at":
          self.updated_at = datetime.fromisoformat(kwargs.get(key))
        elif key == "name":
          self.name = kwargs.get(key)
        else:
          self.my_number = kwargs.get(key)

  def save(self):
    self.updated_at = datetime.now()
    copy_datetime_dict = copy.deepcopy(self.__dict__)
    self.to_dict()
    storage.save()
    self.__dict__ = copy_datetime_dict

  def to_dict(self):
    new_dict = self.__dict__
    """
    convert instance variable created_at and updated_at
    from datetime object to a str object in the format
    %Y-%m-%dT%H:%M:%S.%f e.g 2017-06-14T22:31:03.285259
    using the datetime.isoformat(). 
    an note this also changes the type of the created_at
    and updated_at
    """
    new_dict["created_at"] = self.created_at.isoformat()
    new_dict["updated_at"] = self.updated_at.isoformat()
    """add new key __class__ equating value classname BaseModel as string"""
    new_dict["__class__"] = type(self).__name__
    return new_dict

  def __str__(self):
    return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
