import re
# resultado =

match = re.match('Hello[ \t]*(.*)world', 'Hello'
#resultado =
                 
                 
 match.group(1)
#resultado =
                 

 match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
 #resultado =
                 
                 
 match.groups()
 #resultado = 
                 
 re.split('[/:]', '/usr/home/lumberjack')
#resultado =
                 

 phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
 #resultado =
                 
 mo = phone_num_regex.search('My number is 415-555-4242.')
#resultado = NameError: name 'phone_num_regex' is not defined
                 
                 
                 
 print(f'Phone number found: {mo.group()}')
#resultado = NameError: name 'mo' is not defined
                 
 

 phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#resultado = NameError: name 're' is not defined
                 
                 
 mo = phone_num_regex.search('My number is 415-555-4242.')
 #resultado = NameError: name 'phone_num_regex' is not defined
                 
 mo.group(1)
 #resultado  mo.group(1)
                 
 mo.group(2)
 #resultado = mo.group(2)
                 
 mo.group(0)
 #resultado =  mo.group(0)
                 
 mo.group()
#resltado =  mo.group()
                 
 hero_regex = re.compile (r'Batman|Tina Fey')
 #resltado = NameError: name 're' is not defined
                 
                 
 mo1 = hero_regex.search('Batman and Tina Fey.')
 #resultado = mo1 = hero_regex.search('Batman and Tina Fey.')
                 
 mo1.group()
 #rersultado =  mo1.group()
                 
 mo2 = hero_regex.search('Tina Fey and Batman.')
 #resultado =  mo2 = hero_regex.search('Tina Fey and Batman.')
                 
 mo2.group()
 #resultado = NameError: name 'mo2' is not defined                