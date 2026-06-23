def main():
    """Vector Database Study Project Main Module"""

from vectordb.utils import (
    get_openai_api_key,
    get_pinecone_api_key, 
    get_pinecone_environment,
    load_text_file
)


def main():
    """Main function to test the vector database setup"""
    print("🚀 Vector Database Study Project")
    print("=" * 40)
    
    # Check environment variables
    print("\n📋 Environment Check:")
    
    openai_key = get_openai_api_key()
    if openai_key:
        print("✅ OpenAI API Key: Configured")
    else:
        print("❌ OpenAI API Key: Not found")
    
    pinecone_key = get_pinecone_api_key()
    if pinecone_key:
        print("✅ Pinecone API Key: Configured")
    else:
        print("❌ Pinecone API Key: Not found")
        
    pinecone_env = get_pinecone_environment()
    if pinecone_env:
        print("✅ Pinecone Environment: Configured")
    else:
        print("❌ Pinecone Environment: Not found")
    
    # Test data loading
    print("\n📁 Data Loading Test:")
    finance_keywords = load_text_file("09-VectorStore/data/finance-keywords.txt")
    nlp_keywords = load_text_file("09-VectorStore/data/nlp-keywords.txt")
    
    print(f"📊 Finance keywords loaded: {len(finance_keywords)} items")
    if finance_keywords:
        print(f"   Sample: {finance_keywords[:3]}")
        
    print(f"📊 NLP keywords loaded: {len(nlp_keywords)} items")
    if nlp_keywords:
        print(f"   Sample: {nlp_keywords[:3]}")
    
    print("\n🎯 Ready to start vector database experiments!")
    print("   - Run Jupyter Lab: uv run jupyter lab")
    print("   - Open notebooks in 09-VectorStore/ directory")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
