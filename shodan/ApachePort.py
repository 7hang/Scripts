import shodan
import sys

api=shodan.Shodan("cB9sXwb7l9xxxxxxxxxxxxxQpkzfhQVM")  
try:
    results=api.search('apache')    
    print(results)
    print("Results found:%s"%results['total'])
    for result in results['matches']:
        url = result['ip_str'] + ":" + str(result['port'])
        print(url)

except KeyboardInterrupt:
    print ("Ctrl-c pressed ...")
    sys.exit(1)

except Exception as e:
    print('Error: %s' % e)
    sys.exit(1)
