from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = None


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_length=100)


class MeetingRoomUpdate(MeetingRoomBase):

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя переговорки не может быть пустым!')
        return value


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        from_attributes = True
