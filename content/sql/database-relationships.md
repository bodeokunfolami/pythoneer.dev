Title: Database Relationships Explained
Date: 2023-03-20 12:00
category: python
tags: mysql

A relational database is a widely used database in the world, it organizes data inside a table in the form of rows and columns. A relational database has a predefined structure in which data is organized. Relationships represent connections between two or more tables. Relationships help structure database tables relate with each other. There are three major kinds of relationships found in relational databases, they are:

1. One-to-One
2. One-to-Many
3. Many-to-Many

> One-to-Many relationship is the most common database relationship

### One-to-One Relationship
A One-to-One relationship is used to extend a database table to another table. One-to-one relationships combine the two tables as though they are the same tables. For example, a user table has a one-to-one relationship with a profile table, this means that for every user record, there is exactly one profile record. The user and profile table can have only one record on each side of the relationship.

<center>
![one-to-one img]({static}/images/one-to-one.png)
<center>

In the diagram above, the avatar for the user is stored in the profile table. A user cannot have more than one profile.

The SQL representation of the diagram above.

```sql
CREATE TABLE user (
  userId INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE profile (
  profileId INT PRIMARY KEY AUTO_INCREMENT,
  avatar VARCHAR(50) NULL,
  userId INT UNIQUE NOT NULL
);
```

Define a one-to-one relationship between the user and the profile table

```sql
ALTER TABLE profile
ADD CONSTRAINT FK_user_profile FOREIGN KEY (userId)
REFERENCES user (userId);
```

> This is a one-to-one relationship because the userId was set to UNIQUE for every profile record.

### One-to-Many Relationship
This relationship allows duplicate values in the table, the relationship is defined. This relationship lets a single record from one table be associated with multiple records from another table. For example, When a single post has multiple comments, this can be represented in a database using a one-to-many relationship.

<center>
![one-to-many img]({static}/images/one-to-many.png)
<center>

SQL representation of diagram above

```sql
CREATE TABLE post (
  postId INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  body TEXT NOT NULL
);


CREATE TABLE comment (
  commentId INT PRIMARY KEY AUTO_INCREMENT,
  body TEXT NOT NULL,
  postId INT NOT NULL
);
```

Define the relationship with a foreign key on the postId column in the comment table

```sql
ALTER TABLE comment
ADD CONSTRAINT FK_post_comment FOREIGN KEY (postId)
REFERENCES post (postId);
```
The foreign key constraint will relate each record in the comment table to a single record in the post table.

### Many-to-Many Relationship
This relationship is used when multiple records in one table are associated with multiple records in another table. An example of a many-to-many relationship is the relationship between posts and tags, any number of posts can have any number of tags. We can have multiple post records and at the same time multiple tags related to each other. A Many-to-Many relationship is created with two foreign key constraints from the junction table to the individual tables involved in the relationship. A junction table is a separate table used to track a many-to-many relationship.

<center>
![many-to-many img]({static}/images/many-to-many.png)
<center>

The SQL representation of the diagram above

```sql
CREATE TABLE post (
  postId INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  body TEXT NOT NULL
);

CREATE TABLE tag (
  tagId INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE tagged_items (
  postId INT NOT NULL,
  tagId INT NOT NULL,
);
```

Create the foreign key constraints for the junction table `tagged_items`

```sql
ALTER TABLE tagged_items
ADD CONSTRAINT FK_post_tagged_items FOREIGN KEY (postId)
REFERENCES post (postId);

ALTER TABLE tagged_items
ADD CONSTRAINT FK_tag_tagged_items FOREIGN KEY (tagId)
REFERENCES tag (tagId);
```
The junction table will have two one-to-many relationships, one for the post table and one for the tag table.

### Querying Tables With Relationships
When a table has a relationship with other tables, we can easily query the related table using the `JOIN` statement. The join statements let us look up records in a related table. The join statement needs a link that is, a record that is the same in both tables. We can query related tables with the join statement in three ways, inner, left, and right join. Inner join is the most basic way to join two tables together.

We can query a table with a one-to-one relationship with

```sql
SELECT u.username, p.avatar FROM users AS u
INNER JOIN profile AS p ON u.userId = p.userId
WHERE p.profileId = [id];
```
Similarly, we can also query a one-to-many relationship. for example get all the comments for a particular post.

```sql
SELECT c.body FROM post AS p
INNER JOIN comment AS c ON p.postId = c.postId
WHERE p.postId = [id]; 
```

Querying a many-to-many relationship is similar to that of a one-to-many relationship the only difference it involves tables, so there will be two join statements in a single SQL query.

Database relationships are important in database modeling. A proper database utilizes relationships to minimize duplication of data.