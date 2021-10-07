# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VDY_dFtAOMPFqC4DuLAi4BKdEgBnpa9a

**Task 07: Querying RDF(s)**
"""

#!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
# Visualize the results
from rdflib.plugins.sparql import prepareQuery

ns = Namespace("http://somewhere#")
q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ns:Person
  }
  ''',
  initNs = { "ns": Namespace("http://somewhere#"), "rdfs": RDFS}
)

# RDFLib
print("RDFLib")
for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)):
  print(s)

print("\nSPARQL")
# SPARQL
for r in g.query(q1):
  print(r.Subject)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
# Visualize the results

q1 = prepareQuery('''
  SELECT DISTINCT ?Subject WHERE { 
    {?Subject rdf:type ns:Person. }
    UNION 
    {?s rdfs:subClassOf ns:Person.
    ?Subject rdf:type ?s}
  }
  ''',
  initNs = { "ns": Namespace("http://somewhere#"), "rdf": RDF}
)

# RDFLib
print("RDFLib")
for s,p,o in g.triples((None,RDF.type,ns.Person)):
  print(s)
for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)):
  print(s)

print("\nSPARQL")
# SPARQL
for r in g.query(q1):
  print(r.Subject)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
# Visualize the results
q1 = prepareQuery('''
  SELECT DISTINCT ?Subject ?Property ?x WHERE { 
    {?Subject rdf:type ns:Person.
     ?Subject ?Property ?x}
    UNION 
    {?s rdfs:subClassOf ns:Person.
    ?Subject rdf:type ?s.
    ?Subject ?Property ?x}
  }
  ''',
  initNs = { "ns": Namespace("http://somewhere#"), "rdf": RDF, "rdfs": RDFS }
)

# RDFLib
print("RDFLib")
for s,p,o in g.triples((None,RDF.type,ns.Person)):
  for sub,prop,val in g.triples((s,None,None)):
    print(s,prop,val)
for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)):
  for sub,prop,val in g.triples((s,None,None)):
    print(s,prop,val)

print("\nSPARQL")
# SPARQL
for r in g.query(q1):
    print(r.Subject,r.Property,r.x)

 