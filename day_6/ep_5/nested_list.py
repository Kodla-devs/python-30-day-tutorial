import copy

siparisler = [
    ["mouse", "kulaklık"],
    ["klavye", "monitor"],
    ["ssd", "ram"],
]

print(siparisler[0])
print(siparisler[1])
print(siparisler[2])
print(siparisler[1][1])


sinif = [
    ["ali", 
     [80, 90, 70]
     ],
     ["ahmet",
      [50, 60, 100]
      ],
      ["zeynep",
       [40, 90, 70]
       ]
]

print(sinif[0][1][0])

kopya_sinif = sinif[:]
print(kopya_sinif)

derin_kopya_sinif = copy.deepcopy(sinif)