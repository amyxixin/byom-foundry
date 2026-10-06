# byom-foundry
Example to bring your own model to Microsoft Foundry Agent Service using Azure Machine Learning model endpoint

## Prerequisites:
- Azure Machine Learning workspace
- Microsoft Foundry resource
- API Management resource

## Hosting Open Source Models on Azure Machine Learning Online Endpoint
Using Hugging Face open models with vLLM serving engine, you require a Hugging Face account and its access token (from user settings).
### Steps:
1. Build environment using vLLM image: `az ml environment create -f environment.yml`
2. Create Managed Online Endpoint: `az ml online-endpoint create -f endpoint.yml`
3. Create deployment with appropriate compute to serve model: `az ml online-deployment create -f deployment.yml --all-traffic`
4. Retrieve endpoint URL and authentication key to endpoint: `az ml online-endpoint show -n az ml online-endpoint get-credentials -n`
5. (Test the endpoint with test_model.py)
