# -*- coding: utf-8 -*-

from py2neo.data import Node, Relationship
from py2neo import Graph, GraphError, NodeMatcher, RelationshipMatcher

GRAPH_LABLE_FIELD = 'label'

def graph_create_node(graph, label, name):
    '''
        根据标签创建特定名称的节点
    '''


    if name is None or name == "":
        return

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

    if subject_node is None or object_node is None:
        return

    matcher = RelationshipMatcher(graph)
    rel = matcher.match([subject_node, object_node], predicate).first()
    if rel is None:
        graph.create(Relationship(subject_node, predicate, object_node))

def graph_create_rdf(graph, sub_attrs, pred_attrs, obj_attrs):
    '''创建三元组'''

    if graph is None:
        return

    if not isinstance(sub_attrs, dict) or not isinstance(pred_attrs, dict) or not isinstance(obj_attrs, dict):
        return

    if sub_attrs[GRAPH_LABLE_FIELD] is None or sub_attrs[GRAPH_LABLE_FIELD].strip() == '':
        return

    if pred_attrs[GRAPH_LABLE_FIELD] is None or pred_attrs[GRAPH_LABLE_FIELD].strip() == '':
        return

    if obj_attrs[GRAPH_LABLE_FIELD] is None or obj_attrs[GRAPH_LABLE_FIELD].strip() == '':
        return

    label = sub_attrs[GRAPH_LABLE_FIELD].strip()
    del sub_attrs[GRAPH_LABLE_FIELD]
    snode = Node(label, **sub_attrs)
    
    label = obj_attrs[GRAPH_LABLE_FIELD].strip()
    del obj_attrs[GRAPH_LABLE_FIELD]
    onode = Node(label, **obj_attrs)
    
    label = pred_attrs[GRAPH_LABLE_FIELD].strip()
    del pred_attrs[GRAPH_LABLE_FIELD]
    rel = Relationship(snode, label, onode, **pred_attrs)

    if graph.exists(rel):
        print('已存在')
        return

    tx = graph.begin()
    tx.create(snode)
    tx.create(onode)
    tx.create(rel)

    tx.commit()