from models.base_model import BaseModel


class State(BaseModel):

  def __init__(self):
    self.name = ""
    super().__init__()
