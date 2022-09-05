
# Classroom API using DRF

Class Management site




## API Reference

#### Get classroom

```http
  GET /classroom       (ReadOnly For Both of them)
```
```http
  POST  or PUT or DELETE /classroom     (For Teachers)
```

|  Description(Respectively)                |
| :------------------------- |
| Get list of all the students and techer from the classroom |
| CRUD operation available for the techer from the classroom |

#### Get classroom user

```http
  GET /classroom/${id}       (ReadOnly For Both of them)
```
```http
  POST  or PUT or DELETE /classroom/${id}     (For Teachers)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Get each user detail in that classroom |



#### Get created assignment list

```http
  GET /created-assignment       (ReadOnly For Both of them)
```
```http
  POST or PUT or DELETE /created-assignment     (For Teachers)
```


|  Description                |
| :------------------------- |
| Get list of all the task from the created-assignment |

#### Get created-assignment by ID

```http
  GET /created-assignment/${id}       (ReadOnly For Both of them)
```
```http
  POST or PUT or DELETE /created-assignment/${id}     (For Teachers)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Get each specific task |



#### Get completed assignment list

```http
  GET /completed-assignment       (ReadOnly For Both of them)
```
```http
  POST or PUT or DELETE /completed-assignment     (For Teachers)
```


|  Description                |
| :------------------------- |
| Get list of all the task from the completed-assignment |

#### Get completed-assignment by ID

```http
  GET /completed-assignment/${id}       (ReadOnly For Both of them)
```
```http
  POST or PUT or DELETE /completed-assignment/${id}     (For Teachers)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Get each specific completed task |





#### Get notice list (holidays, events)

```http
  GET /notice       (ReadOnly For Both of them)
```
```http
  POST or PUT or DELETE /notice     (For Teachers)
```


|  Description(Respectively)                |
| :------------------------- |
| Get list of all notice created by teachers |
| For the teacher CRUD operation available in notice |
