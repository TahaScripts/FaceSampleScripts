# FaceSampleScripts
This is a set of basic Python scripts for getting started with testing models on HuggingFace via the platform's Inference API.

## Text2Image
From whichever directory you've setup the project, run the following:

    python image.py  -q "query_here" -m "model_name here" -a "auth_token" --compare

Only the **-q** (query) is required to run the command. Takes in [stabilityai/stable-diffusion-2-1]( `(https://huggingface.co/stabilityai/stable-diffusion-2-1)`).
.
Use **-a** flag for your own auth bearer token if you don't want to add to configs.

Output is saved to the export folder.

## Compare Models
An interesting feature is the one for comparing models. Add as many model names as you wish, separated by comma (`,`).

For example the command
`python image.py  -q "Mark Twain attacking Pokemon villagers" -m "stabilityai/stable-diffusion-2-1,prompthero/openjourney" --compare` 
will provide an image from the query (`Mark Twain attacking Pokemon villagers`) for each model provided [ `stabilityai/stable-diffusion-2-1` , `prompthero/openjourney` ].

Output is saved to the export folder.