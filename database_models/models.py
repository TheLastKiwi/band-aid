from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey

Base = declarative_base()


class Band(Base):
    __tablename__ = 'band'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password_hash = Column(String(60))
    location = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    email_verified = Column(Boolean,default=False)


class EmailVerification(Base):
    __tablename__ = "email_verification"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    code = Column(String(8))


class BandMember(Base):
    __tablename__ = 'band_member'
    band_id = Column(Integer, ForeignKey("band.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    admin = Column(Boolean, default=False)


class BandInvite(Base):
    __tablename__ = "band_invite"
    band_id = Column(Integer, ForeignKey("band.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    code = Column(String(8))