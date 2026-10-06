# byom-foundry
Example to bring your own model to Microsoft Foundry Agent Service using Azure Machine Learning model endpoint

## Prerequisites:
- Hugging Face account (for open source models)
- Azure Machine Learning workspace
- Compute quota suitable for model (for this example, the A100 series)
- Microsoft Foundry resource
- API Management resource

## Hosting Open Source Models on Azure Machine Learning Online Endpoint
Using Hugging Face open models with vLLM serving engine, you require a Hugging Face account and its access token (from user settings). The open source model you choose must be compatible with OpenAI completions API. For this example, we are using the Qwen2.5-7B model.
1. Build environment using vLLM image: `az ml environment create -f environment.yml`
2. Create Managed Online Endpoint: `az ml online-endpoint create -f endpoint.yml`
3. Create deployment with appropriate compute to serve model: `az ml online-deployment create -f deployment.yml --all-traffic`
4. Retrieve endpoint URL and authentication key to endpoint: `az ml online-endpoint show -n az ml online-endpoint get-credentials -n`
5. (Test the endpoint with test_model.py)

## Setting up API Management layer
To connect the model endpoint to Foundry, you must have API management attached to the endpoint.
1. Within the API Management resource, APIs -> Add API -> OpenAPI
   - OpenAPI Specification: see byom-apim-spec.json
   - Display Name: ex. Qwen 7b vLLM API
   - Name: ex. qwen-7b-vllm-api
   - Note the base URL for later
2. Add policy to inbound processing
   ```
   <!--
    - Policies are applied in the order they appear.
    - Position <base/> inside a section to inherit policies from the outer scope.
    - Comments within policies are not preserved.
   -->
   <!-- Add policies as children to the <inbound>, <outbound>, <backend>, and <on-error> elements -->
   <policies>
      <!-- Throttle, authorize, validate, cache, or transform the requests -->
      <inbound>
          <set-header name="Authorization" exists-action="override">
              <value>Bearer (insert your AML endpoint key here)</value>
          </set-header>
          <base />
      </inbound>
      <!-- Control if and how the requests are forwarded to services  -->
      <backend>
          <base />
      </backend>
      <!-- Customize the responses -->
      <outbound>
          <base />
      </outbound>
      <!-- Handle exceptions and customize error responses  -->
      <on-error>
          <base />
      </on-error>
   </policies>
   ```
 3. Test the APIM endpoint: `test_apim.py `

## Connect to Foundry project
[Documentation instructions](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/ai-gateway?tabs=api-management&pivots=foundry-portal)

Note that there may be naming convention issues, so the `/` character was removed from the model name parameter for the endpoint.

Finally, the model should appear in your foundry project (Build -> Models), and subsequently the model can be selected when creating your agents.
<img width="1290" height="300" alt="image" src="https://github.com/user-attachments/assets/d30876e2-4042-4803-92d1-a027557aaef0" />
<img width="929" height="298" alt="image" src="https://github.com/user-attachments/assets/620c61e7-bc77-442c-82ad-66b189f1e912" />


