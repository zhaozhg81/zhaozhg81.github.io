#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 10:46:11 2025

@author: zhigenzhao
"""



text=["",
      "Panda and Amur tiger",
      "The USA Boat: People from everywhere come together to make the USA even better!",
      "This picture shows the scene of celebration of spring festival.",
      "Mixed media painting",        
      "Swallows bring the breath of spring, a hundred flowers bloom, and swallows dart through the air—this is our Asian vision of spring。百花齐放，燕子纷飞，春天来了！",
      "This is how I imagine Asia—a place that feels calm and peaceful, with the great Mount Fuji in the background. I love the old building standing in the ocean, the bright moon shining in the sky, soft cherry blossom petals floating in the air, bamboo swaying in the wind, and lanterns casting a warm golden glow. But most of all, I love the Buddha watching over us, his presence shining down from the Sun.",
      "This drawing displayed a scene of a family gathering of Asian American with fresh fruits, snacks, vegetables and a teapot on the table. I called it a tea party because Asian families love to talk to each other around the table with tea and snacks served in the meantime. ",
      "A Deer of Nine Colors is a Chinese Buddhist tale, famously depicted in the Dunhuang cave murals, about a magical multicolored deer who saves a drowning man but is later betrayed for a reward. When the king confronts the deer, its compassion and wisdom move him to spare its life and punish the traitor. The story, preserved in the vibrant wall paintings of the Mogao Caves, conveys timeless lessons about kindness, loyalty, and the consequences of greed.",
      "This project was done by Ruby McAteer at her home. This is her entry paragraph -this garden features an Indian Princess sitting with a village Snake Charmer in the palace garden. As you can see, this picture is based in India and was inspired by a dream I had about the same thing. The buildinga in the background I copied from reference books. Part of the inspiration for this picture came from the interest I have in Indian culture this year. In conclusion I hope everyone who sees it enjoys this picture. ",
      "The Drawing is showing one of the most important traditional chinese festival — Dragon Boat Festival. The festival on the 5th day of the 5th month in the chinese lunar calendar, is to commemorate QU Yuan, an upright and honest poet and politician of the Chu State during the Warring States Period. The two most famous traditions and customs are Dragon Boat races and making and eating Zongzi (a rice dumpling wrapped in bamboo leaves). In the drawing, the crews of zongzi are making their best efforts to win the race.",
      "My daughter nickname is QQ, inspired by the logo of the Tencent messaging app. When I was pregnant with her, I walked with a waddle due to weight gain, much \
      like a penguin—so we affectionately called her QQ. Since she was little, \
      she has loved penguins and has also had a deep appreciation for traditional Chinese \
      porcelain, especially blue-and-white ceramics. In this painting, \
      she creatively combined these two passions by illustrating a blue-and-white \
      porcelain penguin going to school with a backpack. The small penguin in the \
      bottom left corner represents her younger brother, also heading to school, \
      symbolizing sibling bond and growth together. The artwork integrates traditional \
      patterns into the form of a penguin, merging cultural heritage with imaginative \
      expression.",
      "A Snake Year Liquor Set Designed for Solo Enjoyment",
      "This is my water color painting of lantern. this reminds me of Chinese new year. The red color represents good luck. During new years I hang out  with my friends and family. We get red envelope , play and go to the temple to wish for good luck .This is special to me because I like to play with my cousin and have fun.",
      "The Moon Festival is like an Asian Thanksgiving—a time for family, love, and good food. It’s one of my favorite holidays because my parents, my brothers, and I come together to enjoy a big, delicious meal with crabs, mooncakes, and sweet fruit. After dinner, my mom tells us the story of Chang’e, the moon fairy, and her rabbit, just like her parents told her. We laugh, share stories, and look up at the big, bright moon, feeling warm and happy. It’s a special tradition that brings us closer and is a special part of our family and our American life!",
      "Ne Zha I like Ne Zha because he is a very brave young hero. He faces challenges head-on with incredible strength and courage.",
      "We wanted to show some interesting facts from the two Asian/Pacific Island countries we have roots in (China and the Philippines). We shared how their different cultures impact and inspire life in the United States and also showed some of our favorite foods from these countries.",
      "The Dunhuang Buddha wall paintings, found in the Mogao Caves near the Silk Road town of Dunhuang, are among the most remarkable treasures of ancient Buddhist art. Created between the 4th and 14th centuries, these vibrant murals depict scenes from the life of the Buddha, Buddhist sutras, celestial beings, and tales like A Deer of Nine Colors. Blending artistic styles from China, India, and Central Asia, the paintings not only reflect deep spiritual devotion but also offer a vivid glimpse into the cultural exchange and religious life of the time.",
      "No description.",
      "Handwoven blue and white sea turtle, hoped to bring peace and luck.",
      "My art piece is specifically representing the Filipino people. What specifically encouraged me to choose to represent the Filipino people in my painting was my grandmother, who was originally from the Philippines before moving to the United States. I wanted to incorporate Bayanihan, which means being a bayan. The word bayan means town, community, nation, and anything that's close to that. Bayanihan is used to refer to the spirit of communal unity, cooperation, and helping                               your community without the expectation of something in return. So I illustrated a common depiction of Bayanihan,                                       which is a tradition of moving a family’s nipa by using the strength of the community. The Filipino belief of communal unity and supporting your community helped past Filipino immigrants in the USA to build strong communities to survive discrimination and economic hardship. On the side there is a woman who's wearing the traditional Filipino dress, a baro't saya. I also added the national flower of the Philippines, Sampaguita Jasmine. The bright, vibrant colors are to represent the kindness and warmth of the Filipinos.",
      "The Bloom of AAPI is an oil painting representing the many vibrant cultures and diversity of Asian Americans and Pacific Islanders. The piece features a few national flowers of Asia and a rose, representing America. The importance of this piece relies on its highlighting of positive portrayal and thorough representation in media.",
      "Acrylic on Paint",
      "The drawing depicts a South Asian woman draped in a saree. She is surrounded by various flowers, some marigold(found mostly in the southern Asia region) as well as roses and bee balms(native to the North American region). The diversity of the flowers represents her blossoming spirit in two different places---her native place being in the background and the place she has immigrated to being in the foreground.",
      "The oil painting, The Flowing Canvas of Friendship Beyond the Borders, portrays a rendition of the breathtakingly beautiful Ban Gioc-Detian Waterfalls. The cascading falls are located across the borders between Cao Bang Province, Vietnam and China Daxin County, Guangxi, and is the largest transnational waterfall in Asia. The powerful whitewater is surrounded with lush green vegetation, which reflects the power and calm hidden in nature. Embraced by a blanket of captivating foggy-mist and accompanied with stunning green-blue water, the waterfalls also symbolize unity. The falls do not recognize borders; instead, they showcase a peaceful harmony between two countries. This depiction of the landform represents how when kindness and community meet, they create a beautiful friendship among people with different cultures and backgrounds. ",
      "My artwork is a ceramic peony on a tile set in a wooden frame. Peonies, or moran, frequently appeared in Korean artwork, especially during the Joseon dynasty. Specifically, peonies were symbols of wealth and honor. This is reflected in their voluminous layers of pink petals. Additionally, the glaze used for the tile is a color that closely resembles celadon, a gray-green glaze characteristic of the Goryeo dynasty. The wood frame has been stained darker to highlight the flower, and it can be viewed upright or flat. As a Korean-American, I love learning about Korean culture, and I hope my piece makes other people more curious about Korea and its rich history.",
      "No description."                     
]

from gtts import gTTS

for index in range(1,28):
    print( index )
    tts = gTTS(text=text[index], lang='en')
    tts.save("work"+str(index)+".mp3")

