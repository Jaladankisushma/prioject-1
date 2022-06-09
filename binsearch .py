#binary search
def Binary(arr,low,high,ele):
       if high>=low:
	     mid=(high+low)//2
	     if(arr[mid]==ele):
			return mid
	     elif(arr[mid]>ele):
			return Binary(arr,low,mid-1,ele)
	     else:
			return Binary(arr,mid+1,high,ele)
       else:
	     return 0
arr=[12,13,14,15,16,17]
print("the list is",arr)
ele=int(input("enter the element to search"))

output=Binary(arr,0,len(arr)-1,ele)

if output!=0:
	print("the element is found at",output)
else:
	print("element is not present in the list")
	 

	
