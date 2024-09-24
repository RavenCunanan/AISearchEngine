from exa_py import Exa

exa = Exa('Your API Code Here')

def perform_search():
    query = input('Search here: ')
    
    try:
        num_results = int(input('How many results would you like to see? '))
        
        print("\nSearching, please wait...\n")
        response = exa.search(
            query,
            num_results=num_results,
            type='keyword',
            include_domains=['https://www.tiktok.com'],
        )
        
        results_count = len(response.results)
        
        if results_count == 0:
            print("No results found for your query.")
        else:
            print(f"\nTop {results_count} results for '{query}':\n")
            for idx, result in enumerate(response.results, 1):
                print(f"{idx}. {result.title}")
                print(f"URL: {result.url}\n")
    except ValueError:
        print("Please enter a valid number for results.")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    perform_search()
    repeat = input("Would you like to search again? (y/n): ").lower()
    if repeat != 'y':
        print("Goodbye!")
        break
