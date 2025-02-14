"""
Example usage of the Text Gremlin document extraction library.
"""

from pathlib import Path
from document_extractor import extract_text


def stream_example():
    """Example of streaming output mode."""
    print("\nStreaming Output Example:")
    print("-" * 50)
    
    # Process documents in streaming mode
    results = extract_text(
        "sample_docs",
        recursive=True,
        file_types=["pdf", "pptx"]
    )
    
    if results:
        for result in results:
            # Print metadata
            print("\nMetadata:")
            print(f"Timestamp: {result['metadata']['timestamp']}")
            print(f"Version: {result['metadata']['version']}")
            print(f"File Types: {result['metadata']['file_types_processed']}")
            
            # Print document info
            for doc in result['documents']:
                print(f"\nDocument: {doc['file_name']}")
                print(f"Type: {doc['file_type']}")
                print(f"Created: {doc['date_created']}")
                print(f"Modified: {doc['date_modified']}")
                if doc['error']:
                    print(f"Error: {doc['error']}")
                else:
                    # Print first 200 chars of content with ellipsis
                    content_preview = doc['content'][:200] + "..."
                    print(f"Content Preview: {content_preview}")


def file_output_example():
    """Example of file output mode."""
    print("\nFile Output Example:")
    print("-" * 50)
    
    output_file = Path("output") / "extraction_results.json"
    
    # Process documents and write to file
    extract_text(
        "sample_docs",
        output_path=str(output_file),
        output_mode="file",
        recursive=True,
        batch_size=2  # Process 2 documents per batch
    )
    
    print(f"Results written to: {output_file}")


if __name__ == "__main__":
    # Create output directory if it doesn't exist
    Path("output").mkdir(exist_ok=True)
    
    # Run examples
    stream_example()
    file_output_example()