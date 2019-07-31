# DAO and ORM 
## 1. Impedance Mismatch
* The first problem that may occur is that is data type mismatch means **the programming language attribute data type may differ from the attribute data type in the data model.**  
Hence it is quite necessary to have a binding for each host programming language that specifies for each attribute type the compatible programming language types. It is basically necessary to have different data types, for example, we have different data types available in different programming languages such as data types in C are different from Java and both differ from SQL data types.

* The second problem that may occur is because **the results of most queries are sets or multisets of tuples and each tuple is formed of a sequence of attribute values. In the program, it is necessary to access the individual data values within individual tuples for printing or processing.**  
Hence there is a need for binding to map the query result data structure which is basically a table to an appropriate data structure in the programming language. A mechanism is needed to loop over the tuples in a query result in order to access a single tuple at a time and to extract individual values from the tuple.
The extracted values are typically copied to appropriate program variables for further processing by the program.
A cursor or iterator is a variable which is basically used for looping over the tuples in a query result. Individual values within each tuple are basically extracted into different or unique program variables of the appropriate datatype.



## 2. DAO 
* **Define**: A data access object is a pattern that is often followed when an application needs to interact with some persistent data store (often a database).   
* The DAO provides a series of operations to the rest of the application without the application needing to know the details of the data store. For example, there might be operations to retrieve a subset of data, update the data, or remove the data. It is much more generic than ORM - it simply is an object an application uses to retrieve data.


## 3.O/R Mapping 
* **Define**: An ORM usually describes a library/API used to make interactions with a database more robust.  
* Java has an ORM called JPA, which allows you to persist Java objects directly to a database without having to generate your own SQL statements. You generate Java objects (often called entities) that match the columns/tables of a database, populate the Java object, then called persist(object). It knows how to store itself in the database. When you query the database for data, it will return it in the form of Java objects, instead of the nasty ResultSet that you get when you are using JDBC with SQL.

## 3. Conclusion 
DAO is an object that abstract the implementation of a persistent data store away from the application and allows for simple interaction with it. A ORM is a robust library/API that provides a bunch of tools to save/retrieve an object directly to/from the database without having to write your own SQL statements.  

***Note** - they aren't opposing concepts (they actually go together quite well). It isn't uncommon for your DAO to use an ORM.* 