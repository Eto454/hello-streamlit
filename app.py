import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Markdown ถูกใช้เพื่อรูปแบบข้อความและสร้างลิงก์
st.markdown(
    f"""
        <style>
        .stApp {{
            background-image: url("https://i.pinimg.com/originals/94/69/f6/9469f63cb17b971a97b02a54c0e5a962.gif");
            background-attachment: fixed;
            background-size: cover;
            /* opacity: 0.3; */
        }}
        [data-testid="stSidebar"]{{
           background-image: url(https://i.pinimg.com/originals/88/c1/21/88c121cb2582253a16951a43864ebe1f.gif);
           background-size: cover;
        }}
        </style>
        """,
    unsafe_allow_html=True
)
#---------------------------------------------------------------------------------background-------------------------------------------------------------------------------------

# เพิ่มปุ่มใน sidebar
st.sidebar.header('เมนู')
option = st.sidebar.selectbox(
    'เลือกหัวข้อ',
    ('Home', 'Riotgames', 'HoYoverse', 'other','Model')
)

# ตรวจสอบการเลือกและแสดงเนื้อหาที่เกี่ยวข้อง
if option == 'Home':
    st.header('The Game Room', divider='rainbow')
    st.title('Home')
    st.markdown('![image](https://i.pinimg.com/originals/72/e9/c3/72e9c33f3327bfb2485c80b3188e41fb.gif)')

    code = '''
       ("สวัสดีครับ ขอต้อนรับเข้าสู่ The Game Room")'''
    st.code(code, language='python')
    code = '''
          print(" ..ผมเชื่อว่าทุกคนเคยเล่นเกมส์กันมาไม่มากก็น้อย 
                วันนี้ผมรวบรวมเกมส์ดังของแต่ละค่ายหรือ เกมส์ดังที่สนุกๆมานำเสนอไห้ทุกท่านได้รับชม
                ผมก็เลยจะพาทุกๆคนไปดูเกมเเต่ละประเภทกันอย่างคร่าวๆครับว่าจะมีอะไรกันบ้าง")'''
    st.code(code, language='python')

elif option == 'Riotgames':
    st.header('เกมส์ภายในค่าย Riotgames', divider='rainbow')
    st.title('Type')
    st.title('1.League of Legends')
    st.image('https://wpadmin.gamefever.co/wp-content/uploads/2020/01/League-of-Legend.jpg')
    st.caption('LoL หรือ League of Legends คือเกมออนไลน์สไตล์ MOBA ที่ถือกำเนิดขึ้นมาในปี 2009 โดยบริษัท Riot Games โดยได้แรงบันดาลใจมาจากเกม Dota (Defense of the Ancients ที่เป็น Mod ของเกม Warcraft III)หลังจากที่เปิดตัวในปี 2009 ซึ่งช่วงนั้นกำลังเป็นกระแสเกม MOBA มันก็ได้รับความนิยมเป็นอย่างมาก จนกระทั่งในปี 2012 LoL กลายเป็นเกมบน PC ที่มีคนเล่นนานที่สุดหากนับเป็นชั่วโมงในภูมิภาคอเมริกาเหนือ และยุโรป จากนั้นในปี 2014 เกม LoL ได้จารึกหน้าประวัติศาสตร์ด้วยการมีจำนวนผู้เล่นกว่า 67 ล้านคนต่อเดือน, 27 ล้านคนต่อวัน และ 7.5 ล้านคนในทุก ๆ ชั่วโมง ทำให้กลายเป็นเกมที่มีการสตรีมผ่านช่องทางเช่น Youtube และ Twitch มากที่สุดในโลกอีกด้วย')
    st.write('Download >> https://www.leagueoflegends.com/th-th/')
     
    st.title('2.Valorant')
    st.image('https://cdn1.epicgames.com/offer/cbd5b3d310a54b12bf3fe8c41994174f/EGS_VALORANT_RiotGames_S1_2560x1440-055bbe0f10c1778fcbd134f2de02daf6?h=270&quality=medium&resize=1&w=480')
    st.caption('วาโลแรนต์ (Valorant) เป็นวิดีโอเกมผู้เล่นหลายคนที่เล่นฟรี แนววิดีโอเกมยิงมุมมองบุคคลที่หนึ่ง พัฒนาและจัดจำหน่ายโดยไรออตเกมส์ สำหรับไมโครซอฟท์ วินโดวส์ เกมประกาศเปิดตัวเป็นครั้งแรกในเดือนตุลาคม พ.ศ. 2562 ด้วยรหัสว่า โปรเจกต์เอ (Project A) ในช่วงเริ่มแรกโคลสเบต้า ถึงในวันที่ 7 เมษายน พ.ศ. 2563 และเปิดตัวเกมอย่างเป็นทางการในวันที่ 2 มิถุนายน พ.ศ. 2563 หลังมีการพัฒนาเกมมาตั้งแต่ พ.ศ. 2557 วาโลแรนต์ได้รับแรงบันดาลใจจากซีรีย์เกมเคาน์เตอร์-สไตรก์ที่เป็นเกมยิงเชิงกลยุทธ์ (Tactical shooter) ได้นำเอากลไกหลายอย่างมาใช้ เช่น เมนูการซื้อ รูปแบบสเปรย์ และความคลาดเคลื่อนขณะเคลื่อนที่')
    st.write('Download >> https://playvalorant.com/th-th/?gad_source=1&gclid=CjwKCAiA6KWvBhAREiwAFPZM7lCI33YyDs0ZenGVbAfLxUGnObGffbyEeZbWAjm6puDs4HZUM3qObxoCyykQAvD_BwE&gclsrc=aw.ds')

    st.title('3.Legends of Runeterra')
    st.image('https://images.contentstack.io/v3/assets/blt0eb2a2986b796d29/blt693b1a3c58d55a27/65668c6bca38f04b90d309ae/LoR_8B2023_Beyond_RiotBarApplicationSwitcher_660x428.jpg??&format=pjpg&quality=85')
    st.caption('หนึ่งในเกมยุคใหม่ของค่าย Riot Games ที่หลังจากครบรอบ 10 ปีเกม League of Legends ในปีที่ผ่านมา ก็ได้ทำการแตกขยายสาขาเกมของตัวเองออกไปชนกับเกมประเภทอื่นอย่างที่เรียกได้ว่าบ้าบิ่นเลย เพราะแค่วันเดียวพวกเขาก็เปิดตัวเกมมากมายมากกว่า 5 เกม และเกมการ์ดก็เป็นหนึ่งในนั้นกับเกม Legends of Runeterra การ์ดเกมที่สร้างโดยใช้โลกของเกม LoL เป็นพื้นฐานเกม Legends of Runeterra หรือ LoR เป็นเกมการ์ดในแนวทางเดียวกับ Hearthstone คือใช้มานาในการเล่น มี Cost ที่ต้องการของการ์ดแต่ละใบที่แตกต่างกัน และหากใครเคยสัมผัสเกม Hearthstone มาก่อนก็ต้องบอกว่ามีกลิ่นที่คล้ายคลึงกันอยู่ไม่น้อย เพราะ Cost ต่างแล้ว แต่ละใบก็จะมี Health และ Damage ที่ทำได้ด้วยเช่นกัน')
    st.write('Download >> https://playruneterra.com/th-th/?utm_medium=card4%2Bwww.riotgames.com&utm_source=riotbar')

    st.title('4.Teamfight Tactics')
    st.image('https://images.contentstack.io/v3/assets/blt76b5e73bfd1451ea/blt44c78119582ce0a1/655b148c2d2f231296f3a3ea/GameplayOverview_MODULE_03.jpg')
    st.caption('หลังจากที่ประกาศเปิดตัวไปได้ไม่นาน ในที่สุด “Teamfight Tactics” โหมด Auto Chess รายใหม่จาก Riot Game ที่ใช้ธีมของ LoL เป็นพื้นหลังในการสร้าง ก็พร้อมให้ Summoner ทุกท่านได้ลองเล่นเเล้วในเซิร์ฟเวอร์ PBEตามที่ Riot ได้อ้างไว้ ว่า Teamfight Tactics จะไม่เหมือนกัน Auto Chess เเบบเดียวกับ Dota Underlord ของ Valve หรือต้นฉบับ Auto Chess ของ Drodo Studio ซึ่งจากตัวอย่างที่มีผู้เล่นบางคนได้เข้าไปทดสอบเกมกันก่อนเเล้ว ก็เหมือนว่าที่ Riot พูดมาจะเป็นเรื่องจริงอยู่พอสมควร')
    st.write('Download >> https://teamfighttactics.leagueoflegends.com/th-th/?utm_medium=card2%2Bwww.riotgames.com&utm_source=riotbar')

elif option == 'HoYoverse':
    st.header('เกมส์ภายในค่าย HoYoverse', divider='rainbow')
    st.title('Type')
    st.title('1.Honkai Impact 3')
    st.image('https://cdn1.epicgames.com/offer/d2d162953fec40e381867d7af8371362/EGS_HonkaiImpact3rd_miHoYoLimited_S1_2560x1440-960e15b4bc2cf890628fc3c77e4654c6?h=270&quality=medium&resize=1&w=480')
    st.caption('Honkai Impact 3 (ฮงไกอิมแพ็ค 3) เกมมือถือที่ถูกพัฒนาขึ้นโดยบริษัท miHoYo และร่วมเปิดให้บริการโดย Ipocket ได้เปิดให้ลงทะเบียนล่วงหน้าในประเทศโซนเอเชียตะวันออกเฉียงไต้แล้ววันนี้! โดยเกมนี้เป็นเกมที่สร้างขึ้นมาจากมังงะภายใต้ชื่อเดียวกัน และจะเนื้อเรื่องต่อจากภาค Guns Girl ที่มีเนื้อเรื่องเกี่ยวกับการผจญภัยของกลุ่ม Kiana, Raiden Mei และ Bronya ที่ต่อสู้กับ "Honkai" ผ่านการสั่งการรบจากผู้บัญชาการ โดยผู้เล่นจะได้สัมผัสกับการต่อสู้ร่วมกับเหล่านักรบสาววาลคีเรียนั่นเอง')
    st.write('Download >> https://honkaiimpact3.hoyoverse.com/global/en-us/home')

    st.title('2.Genshin Impact')
    st.image('https://assetsio.reedpopcdn.com/Genshin-Impact-4.5-release-date%2C-4.5-Banner-and-event-details-cover.jpg?width=1200&height=1200&fit=bounds&quality=70&format=jpg&auto=webp')
    st.caption(' เป็นเกมผจญภัยในโลกเปิดที่พัฒนาโดย มิโฮโยะ ผู้พัฒนาเกมสัญชาติจีน วางจำหน่ายในระบบปฏิบัติการไมโครซอฟท์วินโดวส์ เพลย์สเตชัน 4 แอนดรอยด์ และไอโอเอส ในเดือนกันยายน พ.ศ. 2563 และได้วางจำหน่ายในเพลย์สเตชัน 5 ในเดือนเมษายน พ.ศ. 2564 นอกจากนี้ยังมีแผนวางจำหน่ายบนนินเท็นโด สวิตช์ในอนาคตอีกด้วย ก็นชินอินแพกต์เป็นเกมรูปแบบโอเพนเวิลด์สไตล์อนิเมะและระบบการต่อสู้แบบแอคชั่น เกมนี้เล่นฟรีและสร้างรายได้ผ่านกลไกเกมกาชา ในขณะที่พัฒนาหลังเกม ฮนไคอิมแพกต์เทิร์ด (พ.ศ. 2559) ด้วยรูปแบบการตั้งชื่อที่คล้ายคลึงกัน แต่ไม่ใช่ภาคต่อสำหรับเกมนี้')
    st.write('Download >> https://genshin.hoyoverse.com/en/home')

    st.title('3.Tears of Themis')
    st.image('https://www.online-station.net/wp-content/uploads/2021/04/1200-64.jpg')
    st.caption('Tears of Themis นำเสนอภาพในรูปแบบ Visual Art คุณภาพสูงและเรื่องราวสุดน่าสนใจ พร้อมเปิดการผจญภัยแห่งความโรแมนติกและการใช้ไหวพริบ โดยผู้เล่นจะสวมบทบาทเป็นทนายความสาว ผู้ใช้ความจริงและความยุติธรรมในการไขคดี ผ่านการสอบปากคำพยานและผู้ต้องสงสัย, ตรวจสอบสถานที่เกิดเหตุ และตรวจสอบหลักฐาน ซึ่งเมื่อรวบรวมพยานหลักฐานได้ครบถ้วนแล้ว ผู้เล่นจะสามารถไปที่ศาลเพื่อเริ่มการต่อสู้ทางกฎหมาย และนำความยุติธรรมและความสงบสุขกลับคืนมาสู่เมือง')
    st.write('Download >> https://tot.hoyoverse.com/en-us')

    st.title('4.Honkai: Star Rail')
    st.image('https://static.thairath.co.th/media/dFQROr7oWzulq5Fa5BISO96nCtu1x9pcl9cVpZmbptabcbnNNtdLAj55mdAzDQB7FZV.webp')
    st.caption('Honkai: Star Rail เป็นเกม Turn-based RPG หรือเกมวางแผน เพื่อโจมตีและต่อสู้กับอีกฝ่ายทีละรอบ โดยในเกมนี้จะให้ผู้เล่นคิดกลยุทธ์ วางแผน ใช้ทักษะพิเศษ หรือเทคนิคการเล่นเฉพาะตัว เพื่อเอาชนะเหล่าศัตรูที่มีจุดอ่อนและจุดแข็งที่ต่างกันออกไปนอกจากจะเน้นการวางแผนต่อสู้กับอีกฝ่าย ในเกมนี้ยังมีเนื้อเรื่องที่น่าสนใจให้เสพ เพิ่มอรรถรสระหว่างเล่นเกม ระบบสุ่มกาชาปอง เพื่อหาตัวละคร กิจกรรมเก็บแต้ม กิจกรรมเอาชนะศัตรู เพื่อรับรางวัลตัวละคร เพชร รวมถึงทรัพยากรในเกมอีกด้วย')
    st.write('Download >> https://hsr.hoyoverse.com/en-us/')

elif option == 'other':
    st.header('เกมส์อื่นๆ อีกมากมายในค่ายเกมส์อีกมากมายที่หยิบยกมาบางเกม', divider='rainbow')
    st.title('Type')
    st.title('1.PUBG')
    st.image('https://bangkokesports.com/wp-content/uploads/2019/02/PUBG-886916-1.jpg')
    st.caption('PUBG นั้นเป็นเกมแนวใหม่ที่เพิ่งเกิดขึ้นได้ไม่นานทำให้มีวิธการเล่นที่ค่อนข้างกับแบบเดิม ๆ ที่เรารู้จักกันมาก่อน โดยการเล่นนั้นจะเป็นแบบทีม 4 คนหรือจะมาเป็นคู่ หรือเดี่ยวก็ได้โดยในหนึ่งแมทช์นั้นจะประกอบไปด้วยผู้เล่นทั้งหมด 100 คนและจะลงไปบนแผนที่ด้วยตัวเปล่าก่อนที่เราจะต้องออกไปหาอุปกรณ์ต่าง ๆ มาใส่เสริมให้ตัวเราเอง นอกจากนี้จะมีตัวกำหนดเลยก็คือ’วง’ ที่จะบีบเข้ามาเรื่อย ๆ เพื่อบังคับให้ผู้เล่นต้องสู้กันเพื่อหาว่าใครหรือกลุ่มไหนจะได้เป็นผู้เหลือรอดสุดท้ายนั่นเอง')
    st.write('Download >> https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/?l=thai')

    st.title('2.Apex Legends')
    st.image('https://img.online-station.net/_content/2019/0207/gallery/1549523662.jpg')
    st.caption('เกม Apex Legends นั้นถูกทดสอบมาหลากหลายรูปแบบเป็นอย่างมากจนในที่สุดพวกเขาก็ได้ข้อพิสูจน์แล้วว่าการเล่นแบบ 3 คนต่อหนึ่งทีมเป็นการเล่นที่ดีที่สุด โดยจะมีตัวให้เลือกทั้งหมด 8 ตัว (มีอีก 3ตัวเพิ่มเข้ามา) ในตอนนี้ ซึ่งคาดเดากันว่าจะมีเพิ่มเติมมากขึ้นอีกในอนาคตข้างหน้า สำหรับแต่และตัวละคร (Legends) นั้นจะมีสกิลทั้งหมด 3 สกิลด้วยกันซึ่งจะต่างกันไปในแต่ละตัว โดยสามารถดูได้ที่บทความ ทักษะตัวละครทั้ง 8 ในหนึ่งการแข่งขันจะมีทีมทั้งหมด 20 ทีมนับเป็นจำนวนผู้เล่น 60 คนต่อการเล่นหนึ่งครั้งซึ่งมีข่าวว่าในอนาคตข้างหน้านอกจากโหมดแบบ 3 คนต่อ 1 ทีมแล้วนั้นจะมีโหมดแบบตะลุยเดี่ยวหรือแบบคู่หูออกมาให้กับผู้เล่นได้เล่นกัน')
    st.write('Download >> https://store.steampowered.com/app/1172470/Apex_Legends/?l=thai')

    st.title('3.Dead by Daylight')
    st.image('https://cdn1.epicgames.com/offer/611482b8586142cda48a0786eb8a127c/EGS_DeadbyDaylight_BehaviourInteractive_S1_2560x1440-a32581cf9948a9a2e24b2ff15c1577c7')
    st.caption('Dead by Daylight เป็นเกมแนวเอาชีวิตรอดแบบสยองขวัญซึ่งสามารถเล่นได้หลายคน โดยรูปแบบการเล่นจะมีทั้งหมด 2 แบบด้วยกัน คือ การสวมบทบาทเป็น Survivor เพื่อหาทางออกและเอาชีวิตรอดจาก Killer ให้ได้ ซึ่ง Survivor จะสามารถร่วมมือกันกับเพื่อนเพื่อเอาชีวิตรอดได้สูงสุดถึง 4 คน ในขณะที่ Killer นั้นจะต้องไล่ล่า Survivor เพียงคนเดียว ')
    st.write('Download >> https://store.steampowered.com/app/381210/Dead_by_Daylight/')

    st.title('4.Terraria')
    st.image('https://www.gamemonday.com/wp-content/uploads/2016/12/TR-Cover-1.jpg')
    st.caption('Terraria คือ ดินแดนแห่งการผจญภัย! ดินแดนแห่งความพิศวง! ดินแดนที่คุณจะได้สร้าง ป้องกัน และ เพลิดเพลินไปกับมัน! ตัวเลือกของคุณใน Terraria มีไม่สิ้นสุด คุณเป็นเกมเมอร์ประเภทนิ้วไวหรือเปล่า หรือว่าเป็นก่อสร้างระดับเทพ เป็นนักสะสม? เป็นนักสำรวจ? มีบางสิ่งเพื่อคุณทุกคน เริ่มต้นด้วยการสร้างที่หลบภัยง่ายๆ จากนั้นก็เริ่มขุดหาสินแร่ หรือทรัพยากรอื่นๆ ค้นพบ และประดิษฐ์ อาวุธเวทมนต์ อาวุธระยะไกล หรืออาวุธประชิดตัวมากหมายหลายหลาก รวมไปถึงชุดเกราะต่างๆ แล้วใช้พวกมันต่อสู้กับศัตรูต่างๆ นับร้อย สักพักคุณก็จะสามารถมุ่งหน้าไปต่อกรกับบอสตัวร้าย หรือจะออกไปตกปลา ขี่สัตว์ ตามหาเกาะลอยฟ้า สร้างบ้านให้ NPC และอื่นๆ อีกเยอะแยะ')
    st.write('Download >> https://store.steampowered.com/app/105600/Terraria/')

    st.title('5.Stardew Valley')
    st.image('https://adaymagazine.com/wp-content/uploads/2021/08/Type-C_stardew-1-1024x683.jpg')
    st.caption('ใน Stardew Valley ผู้เล่นรับบทบาทตัวละครที่ต้องรับฟาร์มของปู่ในสตาร์ดิวแวลลีย์ที่ชำรุดทรุดโทรม ด้วยความที่อยากหนีจากงานในสำนักงานอันเร่งรีบ ขณะหาเงินในเกมเพื่อขยายฟาร์ม ผู้เล่นต้องจัดการกับเวลาและพลังงานของตัวละครระหว่างทำงาน เช่น ปลูกพืชผัก เลี้ยงสัตว์ สร้างของ ขุดเหมือง และเข้าสังคม รวมไปถึงการแต่งงานกับผู้อยู่อาศัยในเมืองเล็กๆ นี้ เกมมีปลายที่เปิดกว้างทำให้ผู้เล่นสามารถทำกิจกรรมได้ตามต้องการ')
    st.write('Download >> https://store.steampowered.com/app/413150/Stardew_Valley/?l=thai')

    st.title('6.dark souls')
    st.image('https://s.isanook.com/ga/0/ud/201/1007305/01.jpg')
    st.caption('“Dark Souls” ชื่อนี้คงคุ้นหูใครหลายๆคนและแน่นอนว่าคนที่เคยเล่นเกมนี้จะต้องมีอาการหัวร้อนกันอย่างแน่นอน และอีกทั้งเนื้อเรื่องในเกมที่ชวนมึนงงชนิดที่ว่าต้องส่ายหัวกันเลยทีเดียว  หากเราเล่นแบบเพลินๆเผลอแป๊บเดียวอาจจะจบเกมไปแล้วโดยที่พลาดเนื้อหาสำคัญๆก็เป็นได้ เพราะพวกรายละเอียดเหล่านี้ถูกผู้สร้างซ่อนอยู่ในตลอดการเดินทางของผู้เล่น วันนี้ผมจึงจะมาเป็นกระบอกเสียงเล็กๆ ที่จะช่วยปะติดปะต่อเรื่องราวของจักรวาล Dark Souls ให้กับผู้อ่านทุกท่านได้เข้าใจมากยิ่งขึ้น ว่าแล้วเราก็มาลุยกับบทแรกกันเลยกับ! “การเริ่มต้นของปฐมเพลิงและมหาสงครามมังกร”')
    st.write('Download >> https://store.steampowered.com/app/570940/DARK_SOULS_REMASTERED/')

    st.title('7.the last of us')
    st.image('https://blog.playstation.com/tachyon/2022/06/14caa8274fc227ae72a0ba394462db2f811e61e6.png?resize=1088%2C612&crop_strategy=smart&zoom=1.5')
    st.caption('สัมผัสเกมที่เป็นที่รักที่เป็นจุดเริ่มต้นของทุกอย่างอีกครั้ง ในอารยธรรมที่ล่มสลาย ที่ที่ผู้ติดเชื้อและผู้รอดชีวิตไร้ซึ่งความเมตตามีอยู่เต็มไปหมด โจเอล ตัวเอกผู้รู้สึกเหน็ดหน่ายได้รับจ้างให้ลักพาตัวเอลลี่ เด็กอายุ 14 ปีออกจากเขตกักกันของทหาร แต่ว่างานเล็กๆ นี้ได้เปลี่ยนเป็นการเดินทางข้ามประเทศที่โหดร้าย ')
    st.write('Download >> https://store.steampowered.com/app/1888930/The_Last_of_Us_Part_I/')

    st.title('8.Fortnite')
    st.image('https://cdn2.unrealengine.com/blade-2560x1440-2560x1440-d4e556fb8166.jpg')
    st.caption('Fortnite นั้นเป็นเกมแนวเอาตัวรอดที่คนเล่นจะต้องร่วมมือกับเพื่อนคนอื่นๆ ที่จะต้องสร้างป้อม ฐานตัวเองขึ้นมา ก่อนพระอาทิตย์ตกดิน ซึ่งพอเข้าสู่ตอนกลางคืน ก็จะมีซอมบี้บุกมาถล่มเรานั่นเอง ตามปกติแล้ว เกมต้องซื้อ แต่สำหรับโหมด Battle Royale นี้จะเป็นโหมดที่เล่นได้ฟรี ดังนั้น จะบอกว่า ในโหมด Battle Royale เป็นกึ่งๆ DEMO ของเกม Fortnite ก็ไม่ผิดนักครับ')
    st.write('Download >> https://store.epicgames.com/th/p/fortnite')

    st.title('9.Dota 2')
    st.image('https://bangkokesports.com/wp-content/uploads/2019/02/0_vbw4wQW_Xq2_3eOo.jpg')
    st.caption('Dota 2 คือเกมส์ออนไลน์ แนว Mutiplayer Online Battle Arena (MOBA) หรือแปลเป็นไทยว่า เกมส์ต่อสู้แบบอารีน่าผู้เล่นหลายคน โดยเกมส์ได้ถูกพัฒนาโดย Valve เจ้าของแพลตฟอร์มจัดจำหน่ายเกมส์ ยักษ์ใหญ่อย่าง Steam รวมถึงเคยพัฒนาเกมส์ดังๆก่อนหน้านี้เช่น Half-Life , Left 4 Dead หรือ Portal โดยเกมส์ Dota 2 ได้ถูกพัฒนาต่อยอดจาก DotA (Defense of the Ancients) Custom Map ที่นิยมมากที่สุดในขณะนั้นของเกมส์ Warcarft III : Frozen Throne ในช่วงปี 2009 โดยเป็นการร่วมมือของ Ice Frog ที่พัฒนา DotA อยู่ในขณะนั้นกับ Valve Corporation ที่เล็งเห็นศักยภาพของตัวเกมส์ที่จะเติบโตขึ้น ในอนาคตข้างหน้า')
    st.write('Download >> https://store.steampowered.com/app/570/Dota_2/')

    st.title('10.ELDEN RING')
    st.image('https://www.gaming.net/wp-content/uploads/2022/12/elden-ring-990x556-1.jpg')
    st.caption('เกมที่ผสมผสานระหว่างดาร์กแฟนตาซีกับแอ็คชัน RPG ซึ่งมาพร้อมกับแผนที่อันกว้างใหญ่และดันเจี้ยนแสนซับซ้อน พบกับเหล่าตัวละครที่มาพร้อมกับเจตนาซ่อนเร้นและเรื่องราวลึกลับ ให้ผู้เล่นได้เพลิดเพลินไปกับการวางแผนกลยุทธ์เพื่อไขปริศนาความลับดินแดนต้องสาปนี้')
    st.write('Download >> https://store.steampowered.com/app/1245620/ELDEN_RING/?l=thai')

    

elif option == 'Model':
    st.title('Model')
    pow = st.selectbox('Choose Game', ['Riotgames','HoYoverse','other'])
    if pow == 'Actionrog':
        volume = st.columns(2)
        player = volume[0].number_input('Type of game', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลผู้เล่น')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('รูป/Ex1.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='player', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินผู้เล่นเเต่ละปี')
        if train:
            st.write('กำลังฝึกประผู้เล่น')
            df = pd.read_excel('รูป/Ex1.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้เล่น')
        if predict:
            df = pd.read_excel('รูป/Ex1.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            target = model.predict([[player]])[0]
            st.write(f"ผู้เล่นในปี {player} จำนวนผู้เล่นประมาณ{target:.2f}ล้านคน")


    if pow == 'Riotgames':
        volume = st.columns(2)
        player = volume[0].number_input('Type of game', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลผู้เล่น')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('รูป/Ex2.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='player', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินผู้เล่นเเต่ละปี')
        if train:
            st.write('กำลังฝึกประผู้เล่น')
            df = pd.read_excel('รูป/Ex2.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้เล่น')
        if predict:
            df = pd.read_excel('รูป/Ex2.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            target = model.predict([[player]])[0]
            st.write(f"ผู้เล่นในปี {player} จำนวนผู้เล่นประมาณ{target:.2f}ล้านคน")


    if pow == 'HoYoverse':
        volume = st.columns(2)
        player = volume[0].number_input('Type of game', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลผู้เล่น')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('รูป/Ex3.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='player', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินผู้เล่นเเต่ละปี')
        if train:
            st.write('กำลังฝึกประผู้เล่น')
            df = pd.read_excel('รูป/Ex3.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้เล่น')
        if predict:
            df = pd.read_excel('รูป/Ex3.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            target = model.predict([[player]])[0]
            st.write(f"ผู้เล่นในปี {player} จำนวนผู้เล่นประมาณ{target:.2f}ล้านคน")



    if pow == 'other':
        volume = st.columns(2)
        player = volume[0].number_input('Type of game', min_value=1)
        colum = st.columns(3)
        load = colum[0].button('โหลดข้อมูลผู้เล่น')
        if load:
            st.write('กำลังโหลดข้อมูล...')
            df = pd.read_excel('รูป/Ex4.xlsx')
            st.write('"Success"')
            st.dataframe(df)
            fig, ax = plt.subplots()
            df.plot.scatter(x='year', y='player', ax=ax)
            st.pyplot(fig)
        train = colum[1].button('ฝึกประเมินผู้เล่นเเต่ละปี')
        if train:
            st.write('กำลังฝึกประผู้เล่น')
            df = pd.read_excel('รูป/Ex4.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            st.write('"Success"')
        predict = colum[2].button('ประเมินผู้เล่น')
        if predict:
            df = pd.read_excel('รูป/Ex4.xlsx')
            model = LinearRegression()
            model.fit(df[['year']], df['player'])
            target = model.predict([[player]])[0]
            st.write(f"ผู้เล่นในปี {player} จำนวนผู้เล่นประมาณ{target:.2f}ล้านคน")



#---------------------------------------------------------------------------------sidebar-------------------------------------------------------------------------------------