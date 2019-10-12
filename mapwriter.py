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
        print(i)
        for j in range(sheet.ncols-1):
            if location=="":
                data[rows[i][0]][head[j+1]]=rows[i][j+1]
            else:
                data[rows[i][0]][location][head[j+1]]=rows[i][j+1]

loc = (r"generalData.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
consts=[] # list of constituencies
# creating the list of constituencies
for i in range(650):
    consts.append(sheet.cell_value(i+1,0))
# initialize a sub dictionary in the data dictionary for each constituency
for i in range(len(consts)):
    data[consts[i]]={}

# Leave Vote data
adddata(r"datasheet.xlsx")





tree = xml.etree.ElementTree.parse('map.xml')

conlist=['Aberavon', 'Aberconwy', 'Aberdeen North', 'Aberdeen South', 'Airdrie and Shotts', 'Aldershot', 'Aldridge-Brownhills', 'Altrincham and Sale West', 'Alyn and Deeside', 'Amber Valley', 'Angus', 'Arfon', 'Argyll and Bute', 'Arundel and South Downs', 'Ashfield', 'Ashford', 'Ashton-under-Lyne', 'Aylesbury', 'Ayr, Carrick and Cumnock', 'Banbury', 'Banff and Buchan', 'Barking', 'Barnsley Central', 'Barnsley East', 'Barrow and Furness', 'Basildon and Billericay', 'Basingstoke', 'Bassetlaw', 'Bath', 'Batley and Spen', 'Battersea', 'Beaconsfield', 'Beckenham', 'Bedford', 'Belfast East', 'Belfast North', 'Belfast South', 'Belfast West', 'Bermondsey and Old Southwark', 'Berwickshire, Roxburgh and Selkirk', 'Berwick-upon-Tweed', 'Bethnal Green and Bow', 'Beverley and Holderness', 'Bexhill and Battle', 'Bexleyheath and Crayford', 'Birkenhead', 'Birmingham, Edgbaston', 'Birmingham, Erdington', 'Birmingham, Hall Green', 'Birmingham, Hodge Hill', 'Birmingham, Ladywood', 'Birmingham, Northfield', 'Birmingham, Perry Barr', 'Birmingham, Selly Oak', 'Birmingham, Yardley', 'Bishop Auckland', 'Blackburn', 'Blackley and Broughton', 'Blackpool North and Cleveleys', 'Blackpool South', 'Blaenau Gwent', 'Blaydon', 'Blyth Valley', 'Bognor Regis and Littlehampton', 'Bolsover', 'Bolton North East', 'Bolton South East', 'Bolton West', 'Bootle', 'Boston and Skegness', 'Bosworth', 'Bournemouth East', 'Bournemouth West', 'Bracknell', 'Bradford East', 'Bradford South', 'Bradford West', 'Braintree', 'Brecon and Radnorshire', 'Brent Central', 'Brent North', 'Brentford and Isleworth', 'Brentwood and Ongar', 'Bridgend', 'Bridgwater and West Somerset', 'Brigg and Goole', 'Brighton, Kemptown', 'Brighton, Pavilion', 'Bristol East', 'Bristol North West', 'Bristol South', 'Bristol West', 'Broadland', 'Bromley and Chislehurst', 'Bromsgrove', 'Broxbourne', 'Broxtowe', 'Buckingham', 'Burnley', 'Burton', 'Bury North', 'Bury South', 'Bury St Edmunds', 'Caerphilly', 'Caithness, Sutherland and Easter Ross', 'Calder Valley', 'Camberwell and Peckham', 'Camborne and Redruth', 'Cambridge', 'Cannock Chase', 'Canterbury', 'Cardiff Central', 'Cardiff North', 'Cardiff South and Penarth', 'Cardiff West', 'Carlisle', 'Carmarthen East and Dinefwr', 'Carmarthen West and South Pembrokeshire', 'Carshalton and Wallington', 'Castle Point', 'Central Ayrshire', 'Central Devon', 'Central Suffolk and North Ipswich', 'Ceredigion', 'Charnwood', 'Chatham and Aylesford', 'Cheadle', 'Chelmsford', 'Chelsea and Fulham', 'Cheltenham', 'Chesham and Amersham', 'Chesterfield', 'Chichester', 'Chingford and Woodford Green', 'Chippenham', 'Chipping Barnet', 'Chorley', 'Christchurch', 'Cities of London and Westminster', 'City of Chester', 'City of Durham', 'Clacton', 'Cleethorpes', 'Clwyd South', 'Clwyd West', 'Coatbridge, Chryston and Bellshill', 'Colchester', 'Colne Valley', 'Congleton', 'Copeland', 'Corby', 'Coventry North East', 'Coventry North West', 'Coventry South', 'Crawley', 'Crewe and Nantwich', 'Croydon Central', 'Croydon North', 'Croydon South', 'Cumbernauld, Kilsyth and Kirkintilloch East', 'Cynon Valley', 'Dagenham and Rainham', 'Darlington', 'Dartford', 'Daventry', 'Delyn', 'Denton and Reddish', 'Derby North', 'Derby South', 'Derbyshire Dales', 'Devizes', 'Dewsbury', 'Don Valley', 'Doncaster Central', 'Doncaster North', 'Dover', 'Dudley North', 'Dudley South', 'Dulwich and West Norwood', 'Dumfries and Galloway', 'Dumfriesshire, Clydesdale and Tweeddale', 'Dundee East', 'Dundee West', 'Dunfermline and West Fife', 'Dwyfor Meirionnydd', 'Ealing Central and Acton', 'Ealing North', 'Ealing, Southall', 'Easington', 'East Antrim', 'East Devon', 'East Dunbartonshire', 'East Ham', 'East Hampshire', 'East Kilbride, Strathaven and Lesmahagow', 'East Londonderry', 'East Lothian', 'East Renfrewshire', 'East Surrey', 'East Worthing and Shoreham', 'East Yorkshire', 'Eastbourne', 'Eastleigh', 'Eddisbury', 'Edinburgh East', 'Edinburgh North and Leith', 'Edinburgh South', 'Edinburgh South West', 'Edinburgh West', 'Edmonton', 'Ellesmere Port and Neston', 'Elmet and Rothwell', 'Eltham', 'Enfield North', 'Enfield, Southgate', 'Epping Forest', 'Epsom and Ewell', 'Erewash', 'Erith and Thamesmead', 'Esher and Walton', 'Exeter', 'Falkirk', 'Fareham', 'Faversham and Mid Kent', 'Feltham and Heston', 'Fermanagh and South Tyrone', 'Filton and Bradley Stoke', 'Finchley and Golders Green', 'Folkestone and Hythe', 'Forest of Dean', 'Foyle', 'Fylde', 'Gainsborough', 'Garston and Halewood', 'Gateshead', 'Gedling', 'Gillingham and Rainham', 'Glasgow Central', 'Glasgow East', 'Glasgow North', 'Glasgow North East', 'Glasgow North West', 'Glasgow South', 'Glasgow South West', 'Glenrothes', 'Gloucester', 'Gordon', 'Gosport', 'Gower', 'Grantham and Stamford', 'Gravesham', 'Great Grimsby', 'Great Yarmouth', 'Greenwich and Woolwich', 'Guildford', 'Hackney North and Stoke Newington', 'Hackney South and Shoreditch', 'Halesowen and Rowley Regis', 'Halifax', 'Haltemprice and Howden', 'Halton', 'Hammersmith', 'Hampstead and Kilburn', 'Harborough', 'Harlow', 'Harrogate and Knaresborough', 'Harrow East', 'Harrow West', 'Hartlepool', 'Harwich and North Essex', 'Hastings and Rye', 'Havant', 'Hayes and Harlington', 'Hazel Grove', 'Hemel Hempstead', 'Hemsworth', 'Hendon', 'Henley', 'Hereford and South Herefordshire', 'Hertford and Stortford', 'Hertsmere', 'Hexham', 'Heywood and Middleton', 'High Peak', 'Hitchin and Harpenden', 'Holborn and St Pancras', 'Hornchurch and Upminster', 'Hornsey and Wood Green', 'Horsham', 'Houghton and Sunderland South', 'Hove', 'Huddersfield', 'Huntingdon', 'Hyndburn', 'Ilford North', 'Ilford South', 'Inverclyde', 'Inverness, Nairn, Badenoch and Strathspey', 'Ipswich', 'Isle of Wight', 'Islington North', 'Islington South and Finsbury', 'Islwyn', 'Jarrow', 'Keighley', 'Kenilworth and Southam', 'Kensington', 'Kettering', 'Kilmarnock and Loudoun', 'Kingston and Surbiton', 'Kingston upon Hull East', 'Kingston upon Hull North', 'Kingston upon Hull West and Hessle', 'Kingswood', 'Kirkcaldy and Cowdenbeath', 'Knowsley', 'Lagan Valley', 'Lanark and Hamilton East', 'Lancaster and Fleetwood', 'Leeds Central', 'Leeds East', 'Leeds North East', 'Leeds North West', 'Leeds West', 'Leicester East', 'Leicester South', 'Leicester West', 'Leigh', 'Lewes', 'Lewisham East', 'Lewisham West and Penge', 'Lewisham, Deptford', 'Leyton and Wanstead', 'Lichfield', 'Lincoln', 'Linlithgow and East Falkirk', 'Liverpool, Riverside', 'Liverpool, Walton', 'Liverpool, Wavertree', 'Liverpool, West Derby', 'Livingston', 'Llanelli', 'Loughborough', 'Louth and Horncastle', 'Ludlow', 'Luton North', 'Luton South', 'Macclesfield', 'Maidenhead', 'Maidstone and The Weald', 'Makerfield', 'Maldon', 'Manchester Central', 'Manchester, Gorton', 'Manchester, Withington', 'Mansfield', 'Meon Valley', 'Meriden', 'Merthyr Tydfil and Rhymney', 'Mid Bedfordshire', 'Mid Derbyshire', 'Mid Dorset and North Poole', 'Mid Norfolk', 'Mid Sussex', 'Mid Ulster', 'Mid Worcestershire', 'Middlesbrough', 'Middlesbrough South and East Cleveland', 'Midlothian', 'Milton Keynes North', 'Milton Keynes South', 'Mitcham and Morden', 'Mole Valley', 'Monmouth', 'Montgomeryshire', 'Moray', 'Morecambe and Lunesdale', 'Morley and Outwood', 'Motherwell and Wishaw', 'Na h-Eileanan An Iar', 'Neath', 'New Forest East', 'New Forest West', 'Newark', 'Newbury', 'Newcastle upon Tyne Central', 'Newcastle upon Tyne East', 'Newcastle upon Tyne North', 'Newcastle-under-Lyme', 'Newport East', 'Newport West', 'Newry and Armagh', 'Newton Abbot', 'Normanton, Pontefract and Castleford', 'North Antrim', 'North Ayrshire and Arran', 'North Cornwall', 'North Devon', 'North Dorset', 'North Down', 'North Durham', 'North East Bedfordshire', 'North East Cambridgeshire', 'North East Derbyshire', 'North East Fife', 'North East Hampshire', 'North East Hertfordshire', 'North East Somerset', 'North Herefordshire', 'North Norfolk', 'North Shropshire', 'North Somerset', 'North Swindon', 'North Thanet', 'North Tyneside', 'North Warwickshire', 'North West Cambridgeshire', 'North West Durham', 'North West Hampshire', 'North West Leicestershire', 'North West Norfolk', 'North Wiltshire', 'Northampton North', 'Northampton South', 'Norwich North', 'Norwich South', 'Nottingham East', 'Nottingham North', 'Nottingham South', 'Nuneaton', 'Ochil and South Perthshire', 'Ogmore', 'Old Bexley and Sidcup', 'Oldham East and Saddleworth', 'Oldham West and Royton', 'Orkney and Shetland', 'Orpington', 'Oxford East', 'Oxford West and Abingdon', 'Paisley and Renfrewshire North', 'Paisley and Renfrewshire South', 'Pendle', 'Penistone and Stocksbridge', 'Penrith and The Border', 'Perth and North Perthshire', 'Peterborough', 'Plymouth, Moor View', 'Plymouth, Sutton and Devonport', 'Pontypridd', 'Poole', 'Poplar and Limehouse', 'Portsmouth North', 'Portsmouth South', 'Preseli Pembrokeshire', 'Preston', 'Pudsey', 'Putney', 'Rayleigh and Wickford', 'Reading East', 'Reading West', 'Redcar', 'Redditch', 'Reigate', 'Rhondda', 'Ribble Valley', 'Richmond (Yorks)', 'Richmond Park', 'Rochdale', 'Rochester and Strood', 'Rochford and Southend East', 'Romford', 'Romsey and Southampton North', 'Ross, Skye and Lochaber', 'Rossendale and Darwen', 'Rother Valley', 'Rotherham', 'Rugby', 'Ruislip, Northwood and Pinner', 'Runnymede and Weybridge', 'Rushcliffe', 'Rutherglen and Hamilton West', 'Rutland and Melton', 'Saffron Walden', 'Salford and Eccles', 'Salisbury', 'Scarborough and Whitby', 'Scunthorpe', 'Sedgefield', 'Sefton Central', 'Selby and Ainsty', 'Sevenoaks', 'Sheffield Central', 'Sheffield South East', 'Sheffield, Brightside and Hillsborough', 'Sheffield, Hallam', 'Sheffield, Heeley', 'Sherwood', 'Shipley', 'Shrewsbury and Atcham', 'Sittingbourne and Sheppey', 'Skipton and Ripon', 'Sleaford and North Hykeham', 'Slough', 'Solihull', 'Somerton and Frome', 'South Antrim', 'South Basildon and East Thurrock', 'South Cambridgeshire', 'South Derbyshire', 'South Dorset', 'South Down', 'South East Cambridgeshire', 'South East Cornwall', 'South Holland and The Deepings', 'South Leicestershire', 'South Norfolk', 'South Northamptonshire', 'South Ribble', 'South Shields', 'South Staffordshire', 'South Suffolk', 'South Swindon', 'South Thanet', 'South West Bedfordshire', 'South West Devon', 'South West Hertfordshire', 'South West Norfolk', 'South West Surrey', 'South West Wiltshire', 'Southampton, Itchen', 'Southampton, Test', 'Southend West', 'Southport', 'Spelthorne', 'St Albans', 'St Austell and Newquay', 'St Helens North', 'St Helens South and Whiston', 'St Ives', 'Stafford', 'Staffordshire Moorlands', 'Stalybridge and Hyde', 'Stevenage', 'Stirling', 'Stockport', 'Stockton North', 'Stockton South', 'Stoke-on-Trent Central', 'Stoke-on-Trent North', 'Stoke-on-Trent South', 'Stone', 'Stourbridge', 'Strangford', 'Stratford-on-Avon', 'Streatham', 'Stretford and Urmston', 'Stroud', 'Suffolk Coastal', 'Sunderland Central', 'Surrey Heath', 'Sutton and Cheam', 'Sutton Coldfield', 'Swansea East', 'Swansea West', 'Tamworth', 'Tatton', 'Taunton Deane', 'Telford', 'Tewkesbury', 'The Cotswolds', 'The Wrekin', 'Thirsk and Malton', 'Thornbury and Yate', 'Thurrock', 'Tiverton and Honiton', 'Tonbridge and Malling', 'Tooting', 'Torbay', 'Torfaen', 'Torridge and West Devon', 'Totnes', 'Tottenham', 'Truro and Falmouth', 'Tunbridge Wells', 'Twickenham', 'Tynemouth', 'Upper Bann', 'Uxbridge and South Ruislip', 'Vale of Clwyd', 'Vale of Glamorgan', 'Vauxhall', 'Wakefield', 'Wallasey', 'Walsall North', 'Walsall South', 'Walthamstow', 'Wansbeck', 'Wantage', 'Warley', 'Warrington North', 'Warrington South', 'Warwick and Leamington', 'Washington and Sunderland West', 'Watford', 'Waveney', 'Wealden', 'Weaver Vale', 'Wellingborough', 'Wells', 'Welwyn Hatfield', 'Wentworth and Dearne', 'West Aberdeenshire and Kincardine', 'West Bromwich East', 'West Bromwich West', 'West Dorset', 'West Dunbartonshire', 'West Ham', 'West Lancashire', 'West Suffolk', 'West Tyrone', 'West Worcestershire', 'Westminster North', 'Westmorland and Lonsdale', 'Weston-Super-Mare', 'Wigan', 'Wimbledon', 'Winchester', 'Windsor', 'Wirral South', 'Wirral West', 'Witham', 'Witney', 'Woking', 'Wokingham', 'Wolverhampton North East', 'Wolverhampton South East', 'Wolverhampton South West', 'Worcester', 'Workington', 'Worsley and Eccles South', 'Worthing West', 'Wrexham', 'Wycombe', 'Wyre and Preston North', 'Wyre Forest', 'Wythenshawe and Sale East', 'Yeovil', 'Ynys Môn', 'York Central', 'York Outer']

cons=tree.findall('''.//*[@class='constit']''')
misses=[]
def swaporder(string):
    space=string.index(" ")
    firsthalf=string[0:space]
    secondhalf=string[space+1:len(string)]
    return secondhalf+" "+firsthalf
for i in cons:
    con=i.getchildren()[0].text
    #i.set("style",r"visibility:visible;fill:green;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:0.8")
    if con not in conlist:
        if ("South" in con) or ("West" in con) or ("North" in con) or ("East" in con) or ("Mid" in con) or ("Central" in con):
            if swaporder(con) in conlist:
                i.set("id",swaporder(con))
                i.getchildren()[0].text=swaporder(con)
    else:
        i.set("id",con)
        
    #i.set("id","con")
    #.attrib to read
"""
for i in cons:
    con=i.attrib["id"]
    if data[con]=={}:
        data[con]['Leave Vote']=0
    i.set("style",r"visibility:visible;fill:rgb(0,0,"+str((data[con]["Leave Vote"])*400-80)+r");fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:none;stroke-opacity:0.8")
    i.getchildren()[0].text=i.getchildren()[0].text+" "+str(data[con]["Leave Vote"])
#print(misses)
"""
tree.write('mapids.xml')
