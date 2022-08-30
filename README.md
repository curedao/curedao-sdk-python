# The CureDAO Python API Client

## Authentication

To use the CureDAO API, you first need to get an access token as described below.  Once you have the token, include it in any of the [API requests documented here](https://curedao.org/api-docs) using the `Authorization` header in the format `Bearer YOUR_TOKEN_HERE`.

### Option 1: Use Demo Data 
If you don't have your own data yet, you can use the access token `demo` in the `Authorization` header in the format `Bearer demo`.

### Option 2: Access Your Own Data
- Go to the [Settings](https://app.curedao.org/#/app/settings)
- Click copy your Personal Access Token
- Include it in your [API requests](https://curedao.org/api-docs) using the `Authorization` header in the format `Bearer YOUR_TOKEN_HERE`

### Option 3: Use it in Your Own App
- Go to the [App Builder](https://builder.curedao.org/#/app/configuration)
- Click `New App` and fill out the form
- Follow the OAuth integration instructions in the `Integration Guide` link

## Common API Usage Examples
- [Get Units](https://curedao.readme.io/reference/getunits)
- [Get Variables](https://curedao.readme.io/reference/getvariables)
- [Get Variable Categories](https://curedao.readme.io/reference/getvariablecategories)
- [Get a Specific Variable](https://curedao.readme.io/reference/getvariables)
- [Save a Measurement](https://curedao.readme.io/reference/postmeasurements)
- [Get Measurements](https://curedao.readme.io/reference/getmeasurements)

## [Get Variables](https://curedao.readme.io/reference/getvariables)
![How to Get Variables](https://user-images.githubusercontent.com/2808553/187514806-a3261932-106a-49b9-b760-2b4b52b384c7.png)

## [Get a Specific Variable](https://curedao.readme.io/reference/getvariables)
![How to Get a Variable](https://user-images.githubusercontent.com/2808553/187515384-cb1a721b-4534-4e5c-9c94-544288b49780.png)

## [Save a Measurement](https://curedao.readme.io/reference/postmeasurements)
![Save a Measurement](https://user-images.githubusercontent.com/2808553/187521885-e9e1dee3-c07c-4073-a503-315ce345fc52.png)

## [Get Measurements](https://curedao.readme.io/reference/getmeasurements)
![Get Measurements](https://user-images.githubusercontent.com/2808553/187522064-9f176e08-53f4-47cb-8084-8feb8cdb3428.png)


