def urlify(string):

#str='md siddiqul hasan'
  lower_case= string.lower()
  url = lower_case.replace(' ', ' - ')
  return url
print(urlify('md siddiqul hasan'))