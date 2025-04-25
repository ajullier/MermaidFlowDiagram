from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class DiagramHeader(Base):
    __tablename__ = 'diagram_headers'
    
    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    GraphTypeID = Column(Integer, ForeignKey('graph_types.ID'))
    
    graph_type = relationship("GraphType", back_populates="diagram_headers")
    nodes = relationship("Node", back_populates="header")

class GraphType(Base):
    __tablename__ = 'graph_types'
    
    ID = Column(Integer, primary_key=True)
    Code = Column(String)
    Description = Column(String)
    
    diagram_headers = relationship("DiagramHeader", back_populates="graph_type")

class Node(Base):
    __tablename__ = 'nodes'
    
    ID = Column(Integer, primary_key=True)
    HeaderID = Column(Integer, ForeignKey('diagram_headers.ID'))
    Content = Column(String)
    Alias = Column(String)
    FigureID = Column(Integer, ForeignKey('figures.ID'))
    
    header = relationship("DiagramHeader", back_populates="nodes")
    figure = relationship("Figure", back_populates="nodes")
    relationships_as_input = relationship("Relationship", foreign_keys="[Relationship.Input]", back_populates="input_node")
    relationships_as_output = relationship("Relationship", foreign_keys="[Relationship.Output]", back_populates="output_node")

class Figure(Base):
    __tablename__ = 'figures'
    
    ID = Column(Integer, primary_key=True)
    Description = Column(String)
    Initial = Column(String)
    End = Column(String)
    
    nodes = relationship("Node", back_populates="figure")

class Message(Base):
    __tablename__ = 'messages'
    
    ID = Column(Integer, primary_key=True)
    Description = Column(String)
    
    relationships = relationship("Relationship", back_populates="message")

class Relationship(Base):
    __tablename__ = 'relationships'
    
    ID = Column(Integer, primary_key=True)
    Input = Column(Integer, ForeignKey('nodes.ID'))
    Output = Column(Integer, ForeignKey('nodes.ID'))
    MessageID = Column(Integer, ForeignKey('messages.ID'))
    
    input_node = relationship("Node", foreign_keys=[Input], back_populates="relationships_as_input")
    output_node = relationship("Node", foreign_keys=[Output], back_populates="relationships_as_output")
    message = relationship("Message", back_populates="relationships")