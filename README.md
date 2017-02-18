# aodd-server


API Endpoint | Description
------------ | -------------
/api/categories/<string:id> | GET - Single category
/api/categories | GET - All categories
/api/products | GET - All products
/api/users/<string:deviceid> | GET/POST - Single user
/api/products/<string:lat>/<string:long>/<string:distance> | GET- products within distance
/api/getweather/<string:lat>/<string:long> | GET - Current weather forecast
/api/trackevent/<string:lat>/<string:long>/<string:deviceid>/<string:productid> | POST - Single trackevent
