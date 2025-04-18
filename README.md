# UrbanMuse GenAI Content Pipeline  

🚀 **Automatically generate on-brand fashion copy** using Gemini, RAG, and semantic embeddings.  
📖 **Blog Post**: [AI-Powered Content Generation for Fashion Brands](https://sujitdayaljonnakuti.github.io/urbanmuse-blog/)  

## Why?  
Fashion brands struggle with:  
- Slow, expensive manual copywriting  
- Generic AI outputs that dilute brand voice  
- Scaling content for hundreds of products  

This pipeline solves it by **grounding AI in your brand’s truth** via:  
- Retrieval-augmented generation (RAG) from style guides  
- Few-shot prompting with real examples  
- Structured JSON outputs for easy deployment  

## Quick Start  
```python
# Clone repo & install dependencies
git clone https://github.com/yourusername/urbanmuse-genai.git
pip install -r requirements.txt  # Gemini API, sentence-transformers, etc.

# Run the pipeline (example)
python generate.py \
  --product "Vintage Indigo Denim Jacket" \
  --brand_guide ./urbanmuse_style_guide.txt
