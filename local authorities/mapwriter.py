import xml.etree.ElementTree
import xlrd
import matplotlib.pyplot as plt
import json

data={
    }

# TODO: Add data for salary, population, education, house prices and health 

# gets all rows but the top row of a spreadsheet into an array
def getrows(sheet):
    rows=[]
    for i in range(sheet.nrows-1):
        row=[]
        for j in range(sheet.ncols):
            row.append(sheet.cell_value(i+1,j))
        rows.append(row)
    return rows

# adds data to the data object
# TODO: write a very clear, unambigous description of what this does
def adddata(sheet,location="",sheetindex=0):
    loc=sheet
    wb=xlrd.open_workbook(loc)
    sheet=wb.sheet_by_index(sheetindex)

    rows=getrows(sheet)
    head=[]

    # creating an array of the headers to use later
    for i in range(sheet.ncols):
        head.append(sheet.cell_value(0,i))

    for i in range(len(rows)):
        for j in range(sheet.ncols-1):
            if location=="":
                data[rows[i][0]][head[j+1]]=rows[i][j+1]
            else:
                data[rows[i][0]][location][head[j+1]]=rows[i][j+1]


consts=["King's Lynn and West Norfolk","Hertsmere","St Albans","Three Rivers","Forest Heath","Central Bedfordshire","South Cambridgeshire","Brentwood","Chelmsford","Colchester","Epping Forest","Uttlesford","Dacorum","East Hertfordshire","North Hertfordshire","Cambridge","Welwyn Hatfield","Norwich","Breckland","Suffolk Coastal","Tendring","Great Yarmouth","North Norfolk","Waveney","Luton","East Cambridgeshire","Fenland","Huntingdonshire","Braintree","Maldon","Broadland","South Norfolk","Babergh","Mid Suffolk","St Edmundsbury","Castle Point","Rochford","Southend-on-Sea","Ipswich","Bedford","Peterborough","Thurrock","Basildon","Harlow","Broxbourne","Stevenage","Watford","Rushcliffe","Nottingham","Lincoln","Rutland","Derbyshire Dales","North Kesteven","West Lindsey","East Lindsey","Leicester","Bolsover","Chesterfield","Ashfield","Mansfield","Amber Valley","Erewash","South Derbyshire","Harborough","Hinckley and Bosworth","Melton","North West Leicestershire","South Holland","South Kesteven","Daventry","East Northamptonshire","South Northamptonshire","Bassetlaw","Newark and Sherwood","High Peak","North East Derbyshire","Blaby","Charnwood","Oadby and Wigston","Broxtowe","Gedling","Derby","Boston","Kettering","Corby","Northampton","Wellingborough","Bromley","Richmond upon Thames","Kingston upon Thames","Barking and Dagenham","Barnet","Brent","Croydon","Ealing","Enfield","Greenwich","Harrow","Hillingdon","Hounslow","Lewisham","Merton","Newham","Redbridge","Waltham Forest","Camden","Westminster","City of London","Hackney","Hammersmith and Fulham","Haringey","Islington","Kensington and Chelsea","Lambeth","Southwark","Tower Hamlets","Wandsworth","Bexley","Havering","Sutton","Newcastle upon Tyne","Northumberland","County Durham","Darlington","Hartlepool","Redcar and Cleveland","Stockton-on-Tees","Gateshead","North Tyneside","South Tyneside","Sunderland","Middlesbrough","Manchester","Lancaster","Preston","Liverpool","Allerdale","Eden","South Lakeland","Fylde","Ribble Valley","Wyre","Blackpool","Halton","Barrow-in-Furness","Carlisle","Copeland","Wigan","Rossendale","Knowsley","Sefton","St. Helens","Wirral","Cheshire East","Cheshire West and Chester","Warrington","Stockport","Chorley","South Ribble","West Lancashire","Blackburn with Darwen","Bolton","Bury","Oldham","Rochdale","Salford","Tameside","Burnley","Hyndburn","Pendle","Trafford","Aberdeen City","City of Edinburgh","Dundee City","Glasgow City","Angus","Argyll and Bute","Dumfries and Galloway","Highland","Moray","Na h-Eileanan Siar","Orkney Islands","Perth and Kinross","Scottish Borders","South Ayrshire","Stirling","Clackmannanshire","East Ayrshire","East Lothian","Falkirk","Fife","Inverclyde","Midlothian","North Ayrshire","North Lanarkshire","Renfrewshire","South Lanarkshire","West Dunbartonshire","West Lothian","Aberdeenshire","Shetland Islands","East Dunbartonshire","East Renfrewshire","Bracknell Forest","Windsor and Maidenhead","South Bucks","Wycombe","Elmbridge","Epsom and Ewell","Guildford","Reigate and Banstead","Runnymede","Spelthorne","Surrey Heath","Woking","West Berkshire","Wokingham","Aylesbury Vale","Chiltern","Basingstoke and Deane","East Hampshire","Hart","Test Valley","Winchester","Maidstone","Sevenoaks","Tonbridge and Malling","Tunbridge Wells","Cherwell","South Oxfordshire","Vale of White Horse","West Oxfordshire","Mole Valley","Tandridge","Waverley","Horsham","Mid Sussex","Brighton and Hove","Portsmouth","Reading","Southampton","Eastbourne","Canterbury","Oxford","Wealden","Chichester","Isle of Wight","Lewes","Rother","New Forest","Dover","Folkestone and Hythe","Thanet","Arun","Slough","Gosport","Havant","Ashford","Swale","Eastleigh","Fareham","Adur","Hastings","Worthing","Medway","Milton Keynes","Rushmoor","Dartford","Gravesham","Crawley","Bath and North East Somerset","Bournemouth","Bristol, City of","Plymouth","Exeter","Cheltenham","North Somerset","Mid Devon","South Hams","Torridge","West Devon","East Dorset","North Dorset","Purbeck","West Dorset","Cotswold","Mendip","Sedgemoor","South Somerset","Taunton Deane","Isles of Scilly","Cornwall","Torbay","East Devon","North Devon","Teignbridge","Christchurch","Weymouth and Portland","West Somerset","Wiltshire","Forest of Dean","Stroud","Tewkesbury","Poole","South Gloucestershire","Gloucester","Swindon","Cardiff","Isle of Anglesey","Gwynedd","Denbighshire","Ceredigion","Pembrokeshire","Carmarthenshire","Monmouthshire","Powys","Conwy","Wrexham","Swansea","Neath Port Talbot","Bridgend","Rhondda Cynon Taf","Caerphilly","Blaenau Gwent","Torfaen","Merthyr Tydfil","Flintshire","Vale of Glamorgan","Newport","Warwick","Coventry","Herefordshire, County of","Shropshire","Stratford-on-Avon","Malvern Hills","Birmingham","Cannock Chase","Tamworth","Dudley","East Staffordshire","Staffordshire Moorlands","North Warwickshire","Wychavon","Wyre Forest","Lichfield","Newcastle-under-Lyme","South Staffordshire","Stafford","Solihull","Bromsgrove","Stoke-on-Trent","Telford and Wrekin","Nuneaton and Bedworth","Sandwell","Walsall","Wolverhampton","Redditch","Worcester","Rugby","York","Sheffield","Leeds","East Riding of Yorkshire","Craven","Hambleton","Harrogate","Richmondshire","Ryedale","Scarborough","North East Lincolnshire","Barnsley","Doncaster","Rotherham","Wakefield","North Lincolnshire","Selby","Kingston upon Hull, City of","Bradford","Calderdale","Kirklees"]
# list of constituencies
tree = xml.etree.ElementTree.parse('map.svg')
root=tree.getroot()
"""
for i in consts:
    con=tree.findall('''.//*[@id=\''''+i+'''']''')[0]
    con.set("class","la")
"""
# initialize a sub dictionary in the data dictionary for each constituency
for i in range(len(consts)):
    data[consts[i]]={}

adddata(r"datasheet.xlsx")

tree = xml.etree.ElementTree.parse('map.svg')
root=tree.getroot()
la=["King's Lynn and West Norfolk","Hertsmere","St Albans","Three Rivers","Forest Heath","Central Bedfordshire","South Cambridgeshire","Brentwood","Chelmsford","Colchester","Epping Forest","Uttlesford","Dacorum","East Hertfordshire","North Hertfordshire","Cambridge","Welwyn Hatfield","Norwich","Breckland","Suffolk Coastal","Tendring","Great Yarmouth","North Norfolk","Waveney","Luton","East Cambridgeshire","Fenland","Huntingdonshire","Braintree","Maldon","Broadland","South Norfolk","Babergh","Mid Suffolk","St Edmundsbury","Castle Point","Rochford","Southend-on-Sea","Ipswich","Bedford","Peterborough","Thurrock","Basildon","Harlow","Broxbourne","Stevenage","Watford","Rushcliffe","Nottingham","Lincoln","Rutland","Derbyshire Dales","North Kesteven","West Lindsey","East Lindsey","Leicester","Bolsover","Chesterfield","Ashfield","Mansfield","Amber Valley","Erewash","South Derbyshire","Harborough","Hinckley and Bosworth","Melton","North West Leicestershire","South Holland","South Kesteven","Daventry","East Northamptonshire","South Northamptonshire","Bassetlaw","Newark and Sherwood","High Peak","North East Derbyshire","Blaby","Charnwood","Oadby and Wigston","Broxtowe","Gedling","Derby","Boston","Kettering","Corby","Northampton","Wellingborough","Bromley","Richmond upon Thames","Kingston upon Thames","Barking and Dagenham","Barnet","Brent","Croydon","Ealing","Enfield","Greenwich","Harrow","Hillingdon","Hounslow","Lewisham","Merton","Newham","Redbridge","Waltham Forest","Camden","Westminster","City of London","Hackney","Hammersmith and Fulham","Haringey","Islington","Kensington and Chelsea","Lambeth","Southwark","Tower Hamlets","Wandsworth","Bexley","Havering","Sutton","Newcastle upon Tyne","Northumberland","County Durham","Darlington","Hartlepool","Redcar and Cleveland","Stockton-on-Tees","Gateshead","North Tyneside","South Tyneside","Sunderland","Middlesbrough","Manchester","Lancaster","Preston","Liverpool","Allerdale","Eden","South Lakeland","Fylde","Ribble Valley","Wyre","Blackpool","Halton","Barrow-in-Furness","Carlisle","Copeland","Wigan","Rossendale","Knowsley","Sefton","St. Helens","Wirral","Cheshire East","Cheshire West and Chester","Warrington","Stockport","Chorley","South Ribble","West Lancashire","Blackburn with Darwen","Bolton","Bury","Oldham","Rochdale","Salford","Tameside","Burnley","Hyndburn","Pendle","Trafford","Aberdeen City","City of Edinburgh","Dundee City","Glasgow City","Angus","Argyll and Bute","Dumfries and Galloway","Highland","Moray","Na h-Eileanan Siar","Orkney Islands","Perth and Kinross","Scottish Borders","South Ayrshire","Stirling","Clackmannanshire","East Ayrshire","East Lothian","Falkirk","Fife","Inverclyde","Midlothian","North Ayrshire","North Lanarkshire","Renfrewshire","South Lanarkshire","West Dunbartonshire","West Lothian","Aberdeenshire","Shetland Islands","East Dunbartonshire","East Renfrewshire","Bracknell Forest","Windsor and Maidenhead","South Bucks","Wycombe","Elmbridge","Epsom and Ewell","Guildford","Reigate and Banstead","Runnymede","Spelthorne","Surrey Heath","Woking","West Berkshire","Wokingham","Aylesbury Vale","Chiltern","Basingstoke and Deane","East Hampshire","Hart","Test Valley","Winchester","Maidstone","Sevenoaks","Tonbridge and Malling","Tunbridge Wells","Cherwell","South Oxfordshire","Vale of White Horse","West Oxfordshire","Mole Valley","Tandridge","Waverley","Horsham","Mid Sussex","Brighton and Hove","Portsmouth","Reading","Southampton","Eastbourne","Canterbury","Oxford","Wealden","Chichester","Isle of Wight","Lewes","Rother","New Forest","Dover","Folkestone and Hythe","Thanet","Arun","Slough","Gosport","Havant","Ashford","Swale","Eastleigh","Fareham","Adur","Hastings","Worthing","Medway","Milton Keynes","Rushmoor","Dartford","Gravesham","Crawley","Bath and North East Somerset","Bournemouth","Bristol, City of","Plymouth","Exeter","Cheltenham","North Somerset","Mid Devon","South Hams","Torridge","West Devon","East Dorset","North Dorset","Purbeck","West Dorset","Cotswold","Mendip","Sedgemoor","South Somerset","Taunton Deane","Isles of Scilly","Cornwall","Torbay","East Devon","North Devon","Teignbridge","Christchurch","Weymouth and Portland","West Somerset","Wiltshire","Forest of Dean","Stroud","Tewkesbury","Poole","South Gloucestershire","Gloucester","Swindon","Cardiff","Isle of Anglesey","Gwynedd","Denbighshire","Ceredigion","Pembrokeshire","Carmarthenshire","Monmouthshire","Powys","Conwy","Wrexham","Swansea","Neath Port Talbot","Bridgend","Rhondda Cynon Taf","Caerphilly","Blaenau Gwent","Torfaen","Merthyr Tydfil","Flintshire","Vale of Glamorgan","Newport","Warwick","Coventry","Herefordshire, County of","Shropshire","Stratford-on-Avon","Malvern Hills","Birmingham","Cannock Chase","Tamworth","Dudley","East Staffordshire","Staffordshire Moorlands","North Warwickshire","Wychavon","Wyre Forest","Lichfield","Newcastle-under-Lyme","South Staffordshire","Stafford","Solihull","Bromsgrove","Stoke-on-Trent","Telford and Wrekin","Nuneaton and Bedworth","Sandwell","Walsall","Wolverhampton","Redditch","Worcester","Rugby","York","Sheffield","Leeds","East Riding of Yorkshire","Craven","Hambleton","Harrogate","Richmondshire","Ryedale","Scarborough","North East Lincolnshire","Barnsley","Doncaster","Rotherham","Wakefield","North Lincolnshire","Selby","Kingston upon Hull, City of","Bradford","Calderdale","Kirklees"]
#King's Lynn and West Norfolk
cons=tree.findall('''.//*[@class='la']''')
        
#i.set("id","con")
#.attrib["id] to read

max1=0
max2=0
for i in cons:
    con=i.attrib["id"]
    if data[con]=={}:
        data[con]['Variable 1']=0
        data[con]['Variable 2']=0
    if data[con]['Variable 1']>max1:
        max1=data[con]['Variable 1']
    if data[con]['Variable 2']>max2:
        max2=data[con]['Variable 2']


for i in cons:
    con=i.attrib["id"]
    #normalise data
    v1=data[con]['Variable 1']/max1
    v2=data[con]['Variable 2']/max2
    r=255
    g=(1-v1)*255
    b=(1-v2)*255    
    colour="rgb("+str(r)+","+str(g)+","+str(b)+")"
    i.set("style","visibility:visible;fill:"+colour+";fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.1;")
x0=800
y0=300
div=30
for x in range(div):
    for y in range(div):
        rect = xml.etree.ElementTree.Element("ns0:rect")
        #print(rect)
        root.append(rect)
        r=255
        g=(1-x/div)*255
        b=(y/div)*255    
        colour="rgb("+str(r)+","+str(g)+","+str(b)+")"
        style="fill:"+colour+";stroke:\"none\""
        shift=400/div
        tree.findall("ns0:rect")[-1].set("style",style)
        tree.findall("ns0:rect")[-1].set("width",str(shift))
        tree.findall("ns0:rect")[-1].set("height",str(shift))
        tree.findall("ns0:rect")[-1].set("x",str(x0+x*shift))
        tree.findall("ns0:rect")[-1].set("y",str(y0+y*shift))
for t in cons:
    con=t.attrib["id"]
    #normalise data
    v1=data[con]['Variable 1']/max1
    v2=data[con]['Variable 2']/max2
    y=(1-v2)*400
    x=(v1)*400
    circle = xml.etree.ElementTree.Element("ns0:circle")
    title = xml.etree.ElementTree.Element("ns0:title")
    title.text=con
    """
    set1=xml.etree.ElementTree.Element("ns0:set")
    set2=xml.etree.ElementTree.Element("ns0:set")
    set1.set("attributeName","fill")
    set1.set("to","grey")
    set1.set("begin",con+"dot.mouseover")
    set1.set("end",con+"dot.mouseout")
    set2.set("attributeName","fill")
    set2.set("to","grey")
    set2.set("begin",con+".mouseover")
    set2.set("end",con+".mouseout")
    """
    circle.set("cx",str(x0+x))
    circle.set("cy",str(y0+y))
    circle.set("r","5")
    circle.set("id",con+"dot")
    circle.set("class","point")
    #circle.append(set1)
    #circle.append(set2)
    circle.append(title)
    root.append(circle)
    #style="fill:\"grey\";stroke:\"none\""
    #tree.findall("ns0:circle")[len(tree.findall("ns0:cricle"))-1].set("style",style)

tree.write('map2.svg')
