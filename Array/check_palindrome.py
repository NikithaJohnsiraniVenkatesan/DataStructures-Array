def Palindrome(a):
  return a == a[::-1]

a = input(("Enter a string to check:"))
ans = Palindrome(a)

if ans:
  print("yes Its a palindrome")
else:
  print("No da kanna Its not a palindrome")