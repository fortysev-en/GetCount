# GetCount
##for Count API

GetCount is a tool to manage the links generated with Count API and will help you track the real time website visits through those links.

Know more about Count API [here!](https://countapi.xyz/)



##Generate your links by using below url
`https://api.countapi.xyz/create?namespace={website_url}&key={pagename}&value=0`

##Add below url on your website
`https://api.countapi.xyz/update/{website_name}/{pagename}/?amount=1`

call the above link from your webpage, so whenever the webpage is requested, the counter will increament by 1

##Manage your links and track live count by GetCount

`Run the script`

`Input New Link` -> `https://api.countapi.xyz/get/{website_url}/{pagename}`

Data is stored in `total_db.json` in the project dir

To view live count, run the script again and select `View Live Count`
