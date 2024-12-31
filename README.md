# LexNet
Lex = Law in latin 


## Usage
```
1. Start Neo4J desktop and the `lextnet` database
2. export GROQ_API_KEY="..."
3. poetry update graphiti-core && poetry run python lexnet/knowledge_graph.py
```

**Plan** 

First, DAG for laws

Then, a formal verifier for laws

And then, replace lawyers (or at least reduce their needs).

**Motivation**

Paying someone to explain things that you should understand yourself is stupid. 

Being able to add and subtract legislation that affect livelihood should be easy and as close to immediate as feasible. 

Being able to understand (like actually understand) things should be easy. 

Being able to propose changes should be easy. 

Being able to validate that a new legislation can be proposed should be easy. 

In the spirit of the 6th amendment, bureacracy shouldn't get in the way of speediness of actions. Things should be automated (reasonably) to a degree as high as possible. 

## Why DAG?

LexNet is built on the fact thtat the legal framework (should) operates much like a mathematical system. At its core are axiomatic truths - fundamental principles or statutes that underpin the legal system.

Building upon these axioms, laws function similarly to theorems in mathematics. Each law is derived from one or more of these foundational truths, forming a complex network of legal provisions that support and rely on each other.

It's reductive to the complexities of the real world, but that makes this project even more important: bringing objectivity into muddled field that should be objective, fair, and equitable.

- Axiomatic Truths: These can be considered as the root nodes in the DAG. They represent fundamental principles or statutes that form the basis of the legal system.

- Laws as Theorems: Each subsequent law or legal provision can be viewed as a node that is connected to one or more of these axiomatic truths. The connections (edges) represent the logical or legal dependency of one law on another.

- Building Upon Each Other: As in a DAG, each node (law) can have multiple incoming edges (dependencies) from other nodes (laws or axioms). This structure effectively visualizes how laws interconnect and build upon each other, as well as upon foundational principles.

## Project notes

### Scope

- Federal vs state law?
  - Starting out with Federal laws as they are more uniform and seem easy
  - [USCode](https://uscode.house.gov/)
- Maybe focus on a particular area?
  - Criminal law seems cool

### Identifying relationships

- References: Laws often reference other laws. These references create a natural dependency network.
- Amendments and Repeals: Laws that amend or repeal other laws create another type of dependency.
- Hierarchical Structure: Federal laws are often organized in a hierarchical manner (e.g., Titles, Chapters, Sections). This structure can guide the construction of your DAG.

### Building the Model:

- Nodes: Each law or legal provision can be a node. In complex cases, nodes could represent individual clauses or sections.
- Edges: Create directed edges based on dependencies (e.g., an edge from a law to another law it amends).

### Validation Rules:

- Consistency Checks: Implement rules to check for legal consistency, such as ensuring that a law does not contradict or improperly amend another.
- Completeness Checks: Ensure that all references are accounted for and that the legal text is complete.

## Current todo-list

- [ ] Parse [Title 18 Crimes and Criminal Procedure](https://uscode.house.gov/download/download.shtml) XML
- [ ] Form associations via DAG
- [ ] Use DAG to generate recommendations via free form text as to legal validity
