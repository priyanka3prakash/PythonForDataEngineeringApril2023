REST API
Representive State Transfer Protocols
CRUD
Create ----> POST
Read ----> GET
Update
----entire record --> PUT
----one colum in record ---> PATCH
Delete ---> DELETE

        HTTP MEthods
            GET, POST, PUT, CREATE, DELETE, UPDATE,

    - For CRUD operations, it should use HTTP methods like
    	GET  - to retrieve one or more records
    	POST - to create record
    	PUT  - to update an existing record
    	PATCH- to update a specific column in existing record
    	DELETE- to delete a record

    	HEAD - response identical to GET, but without response body
    	CONNECT- establishes a tunnel to server identifier by the target resource
    	OPTIONS- used to describe the communication options for the target resource.
    	TRACE- performs a message loop-back test along the path to the target resource.
    	PATCH- used to apply partial modifications to a resource

    - response can be JSON or XML, atom, OData etc.

    Idempotence - If something is idempotent, then no matter how many times you do it, the result will always be the same.
    1. POST is NOT idempotent.
    2. GET, PUT, DELETE, HEAD, OPTIONS and TRACE are idempotent.

    Nulipotent- GET is so because nothing is added or changed, except logging.

- REST based vs RESTFUL

  - REST based services follow some of the above principles and not all
  - RESTFUL services means it follows all the above principles.

    - Richardson-maturity-model
      - to know level of RESTful your API is.
      - https://developers.redhat.com/blog/2017/09/13/know-how-restful-your-api-is-an-overview-of-the-richardson-maturity-model

- Modules

  urllib
  requests
  http.request
  aiohttp

  pandas
