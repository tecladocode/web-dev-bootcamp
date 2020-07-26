# Introduction to MongoDB

MongoDB[^mongodb] is a document-oriented NoSQL database used for high volume data storage.

NoSQL[^nosql] databases (aka "not only SQL") are non-tabular and store data differently than relational tables. They come in a variety of types based on their data model. The main types are document, key-value, wide-column, and graph.


## How is It Different from SQL Databases?

Relational[^rdbms] databases like MySQL, PostgreSQL primarily use tables, rows, and columns to store data in rigid schemas. MongoDB doesn't use these constructions; instead, it employs a document-driven NoSQL data model. It provides flexible schemas and scales effortlessly with large amounts of data and high user loads.

## Data Model

MongoDB stores data in **documents** similar to **JSON** (JavaScript Object Notation) objects. Each document belongs to a specific **collection** and contains pairs of fields and values. The values can typically be a variety of types like strings, numbers, booleans, arrays, or objects, and their structures typically align with objects developers are working within code.

> If you're familiar with SQL databases, you can think of *collections* as tables and the *documents* as rows in the table.

The following diagram shows the anatomy of a MongoDB document:

![MongoDB data model](./assets/mongo_data_model.svg)

## Feature Sets

NoSQL databases like MongoDB offer many advantages over their SQL counterparts. Here's an overview of the features that aim to give you a glimpse of how MongoDB can make web development easier:

* The size and contents of each document can be different from each other. This flexibility in the data model often leads to faster development cadence.

* The documents don't need to have a schema defined beforehand. Instead, you can create the fields on the fly.

* The JSON-like document model is similar to how you construct classes and objects in different procedural programming languages.

* The data model available within MongoDB allows you to represent hierarchical relationships, to store arrays, and other more complex structures easily.

* MongoDB houses a powerful query language that makes it suitable to be used as a general-purpose database.

## Conclusion

In this section, you've got a basic overview of MongoDB and how NoSQL databases differ from their relational counterparts. Also, you've learned about the data model MongoDB uses and what features it offers that sets it apart from other databases.

In the next section, you'll learn how you can get up and running with MongoDB via MongoDB Compass and Atlas.

[^mongodb]: [What is MongoDB?](https://www.mongodb.com/what-is-mongodb)

[^nosql]: [NoSQL Explained](https://www.mongodb.com/nosql-explained#what-is-nosql)

[^rdbms]: [What is SQL?](https://www.mongodb.com/nosql-explained#what-is-sql)
