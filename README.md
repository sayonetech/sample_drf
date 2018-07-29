### Sample API's using DRF

## Status code
- 200	OK – Everything is working
- 201	OK – New resource has been created
- 204	OK – The resource was successfully deleted	
- 304	Not Modified – The client can use cached data	
- 400	Bad Request – The request was invalid or cannot be served. The exact error should be explained in the error payload. E.g. „The JSON is not valid“
- 401	Unauthorized – The request requires an user authentication
- 403	Forbidden – The server understood the request, but is refusing it or the access is not allowed.
- 404	Not found – There is no resource behind the URI.
- 422	Un-processable Entity – Should be used if the server cannot process the entity, e.g. if an image cannot be formatted or mandatory fields are missing in the payload.
- 500	Internal Server Error – API developers should avoid this error. If an error occurs in the global catch blog, the stack-trace should be logged and not returned as response.


### Setup project for development:

- Clone the project
- Install packages mentioned in the runtime.txt
- Create virtualenv  "python3.6 -m venv <virtual_path>"
- Activate and install requirements.txt
- Create a .env file in the root folder, using env.example as template

Docs link: "http://domain.com>/docs/", it will be enabled only if REST_FRAMEWORK_DOC_ENABLED=True