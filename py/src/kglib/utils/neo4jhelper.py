# -*- coding: utf-8 -*-

from py2neo.data import Node, Relationship
from py2neo import Graph, GraphError, NodeMatcher, RelationshipMatcher

def graph_create_node(graph, label, name):
    '''
        根据标签创建特定名称的节点
    '''

    matcher = NodeMatcher(graph)
    
    node = matcher.match(label, name=name).first()
    if node is None:
        node = Node(label, name=name)
        graph.create(node)

    return node

def graph_create_relation(graph, subject_node, predicate, object_node):
    '''
        创建关系
    '''

    matcher = RelationshipMatcher(graph)
    rel = matcher.match([subject_node, object_node], predicate).first()
    if rel is None:
        graph.create(Relationship(subject_node, predicate, object_node))
