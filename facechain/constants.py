neg_prompt = '(nsfw:2), paintings, sketches, (worst quality:2), (low quality:2), ' \
             'lowers, normal quality, ((monochrome)), ((grayscale)), logo, word, character, bad hand'
pos_prompt_with_cloth = 'raw photo, masterpiece, chinese, {}, solo, medium shot, high detail face, looking straight into the camera with shoulders parallel to the frame, slim body, photorealistic, best quality'
pos_prompt_with_style = '{}, upper_body, raw photo, masterpiece, solo, medium shot, high detail face, slim body, photorealistic, best quality'

base_models = [
    {'name': 'leosamsMoonfilm_filmGrain20',
    'model_id': 'ly261666/cv_portrait_model',
    'revision': 'v2.0',
    'sub_path': "film/film",
    'style_list': ['工作服(Working suit)', '盔甲风(Armor)','T恤衫(T-shirt)','汉服风(Hanfu)','女士晚礼服(Gown)','赛博朋克(Cybernetics punk)','凤冠霞帔(Chinese traditional gorgeous suit)']},
    {'name': 'MajicmixRealistic_v6',
    'model_id': 'YorickHe/majicmixRealistic_v6',
    'revision': 'v1.0.0',
    'sub_path': "realistic",
    'style_list': ['冬季汉服(Chinese winter hanfu)', '校服风(School uniform)', '婚纱风(Wedding dress)', '夜景港风(Hong Kong night style)', '雨夜(Rainy night)', '模特风(Model style)', '机车风(Motorcycle race style)', '婚纱风-2(Wedding dress 2)','拍立得风(Polaroid style)', '仙女风(Fairy style)', '古风(traditional chinese style)', '壮族服装风(Zhuang style)', '欧式田野风(European fields)', '雪山羽绒服风(Jacket in Snow Mountain)', '漫游宇航员(Roaming Astronaut)', '复古军装风(Retro military uniform)', '海港船长风(Sea Captain)']},
]

styles = [
    {'name': '工作服(Working suit)',
     'img': './style_image/Working_suit.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing high-class business/working suit, simple background, high-class pure color background'},
    {'name': '盔甲风(Armor)',
     'img': './style_image/Armor.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing silver armor, simple background, high-class pure color background'},
    {'name': 'T恤衫(T-shirt)',
     'img': './style_image/T-shirt.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing T-shirt, simple background, high-class pure color background'},
    {'name': '汉服风(Hanfu)',
     'img': './style_image/Hanfu.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing beautiful traditional hanfu, upper_body, simple background, high-class pure color background'},
    {'name': '女士晚礼服(Gown)',
     'img': './style_image/Gown.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'wearing an elegant evening gown, simple background, high-class pure color background'},
    {'name': '赛博朋克(Cybernetics punk)',
     'img': './style_image/Cybernetics_punk.jpg',
     'model_id': None,
     'revision': None,
     'bin_file': None,
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'white hair, neon glowing glasses, cybernetics, punks, robotic, AI, NFT art, Fluorescent color, ustration'},
    {'name': '凤冠霞帔(Chinese traditional gorgeous suit)',
     'img': './style_image/Chinese_traditional_gorgeous_suit.jpg',
     'model_id': 'ly261666/civitai_xiapei_lora',
     'revision': 'v1.0.0',
     'bin_file': 'xiapei.safetensors',
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': 'red, hanfu, tiara, crown'},
     {'name': '冬季汉服(Chinese winter hanfu)',
     'img': './style_image/Chinese_winter_hanfu.jpg',
     'model_id': 'YorickHe/Winter_hanfu_lora',
     'revision': 'v1.0.0',
     'bin_file': 'Winter_Hanfu.safetensors',
     'multiplier_style': 0.3,
     'multiplier_human': 0.95,
     'add_prompt_style': 'red hanfu, winter hanfu, cloak, photography, warm light, sunlight, majestic snow scene,  close-up, front view, soft falling snowflakes, jewelry, enchanted winter wonderland'},
     {'name': '校服风(School uniform)',
     'img': './style_image/School_uniform.jpg',
     'model_id': 'YorickHe/JK_uniform_lora',
     'revision': 'v1.0.0',
     'bin_file': 'jk_uniform.safetensors',
     'multiplier_style': 0.2,
     'multiplier_human': 0.95,
     'add_prompt_style': 'JK_style, white short-sleeved JK_shirt, dark blue JK_skirt, bow JK_tie, close-up, looking at viewer, sweet smile, night, Tokyo street, night city scape'},
     {'name': '婚纱风(Wedding dress)',
     'img': './style_image/Wedding_dress.jpg',
     'model_id': 'YorickHe/outdoor_photo_lora',
     'revision': 'v1.0.0',
     'bin_file': 'outdoor_photo_v2.0.safetensors',
     'multiplier_style': 0.3,
     'multiplier_human': 0.95,
     'add_prompt_style': 'white wedding dress, 1girl, summer, flower, happy atmosphere, sunlight, Waist Shot'},
     {'name': '夜景港风(Hong Kong night style)',
     'img': './style_image/Hong_Kong_night_style.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.35,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, close-up, face shot, stylish outfit, fitted jeans, oversized jacket, fashionable accessories, cityscape backdrop, rooftop or high-rise balcony, dynamic composition, engaging pose, soft yet striking lighting, shallow depth of field, bokeh from city lights, naturally blurred background'},
     {'name': '雨夜(Rainy night)',
     'img': './style_image/Rainy_night.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.45,
     'multiplier_human': 0.95,
     'add_prompt_style': 'standing in the rain, wet, wet clothes, wet hair, face Shot, front view, close-up, cityscape, cold lighting, realistic, cinematic lighting, photon mapping, radiosity, physically-based rendering'},
     {'name': '模特风(Model style)',
     'img': './style_image/Model_style.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.3,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, balenciaga, close-up, fashion, streets of new york, new york, modeling for Balenciaga, natural skin texture, dynamic pose, rouge, film grain'},
     {'name': '机车风(Motorcycle race style)',
     'img': './style_image/Motorcycle_race_style.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.4,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, close-up, wearing racing clothes, motorbike clothes, modeling, playful, futuristic, city street background, at night, cool atmospheric, realistic'},
     {'name': '婚纱风-2(Wedding dress 2)',
     'img': './style_image/Wedding_dress_2.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.4,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, close-up, wearing wedding dress, white, film grain, sunlight, sun flare, lens flare, field of white roses, high fashion, top model'},
    {'name': '拍立得风(Polaroid style)',
     'img': './style_image/Polaroid_style.jpg',
     'model_id': 'YorickHe/polaroid_lora',
     'revision': 'v1.0.0',
     'bin_file': 'InstantPhotoX3.safetensors',
     'multiplier_style': 0.4,
     'multiplier_human': 0.95,
     'add_prompt_style': '1girl, close-up, simple clothes, front view, looking straight into the camera, film grain, flash, enhanced flash, dark background, polaroid, instant photo, realistic face'},
     {'name': '仙女风(Fairy style)',
     'img': './style_image/Fairy_style.jpg',
     'model_id': 'YorickHe/fairy_lora',
     'revision': 'v1.0.0',
     'bin_file': 'fairy.safetensors',
     'multiplier_style': 0.25,
     'multiplier_human': 0.95,
     'add_prompt_style': 'a beautiful fairy standing in the middle of a flower field, petals, close-up, warm light, light green atmosphere, white atmosphere, in the style of celebrity photography, soft, romantic scenes, flowing fabrics, light white and light orange, high resolution'},
     {'name': '古风(traditional chinese style)',
     'img': './style_image/traditional_chinese_style.jpg',
     'model_id': 'iotang/lora_testing',
     'revision': 'v5',
     'bin_file': 'MoXinV1.safetensors',
     'multiplier_style': 0.3,
     'multiplier_human': 0.95,
     'add_prompt_style': '(ultra high res face, face ultra zoom, highres, best quality, ultra detailed, cinematic lighting, portrait, Chinese traditional ink painting:1.2), sfw, shuimobysim, song, anxiang, hanfu, Ultra HD, wuchangshuo, detailed background, looking at viewer, serenity, peace'},
    {'name': '壮族服装风(Zhuang style)',
     'img': './style_image/Zhuang_style.jpg',
     'model_id': 'iotang/lora_testing',
     'revision': 'v5',
     'bin_file': 'zhuangnv.safetensors',
     'multiplier_style': 0.7,
     'multiplier_human': 0.95,
     'add_prompt_style': '(masterpiece, ultra high res face, face ultra zoom, highres, best quality, ultra detailed, cinematic lighting, portrait:1.2), sfw, facing the camera with a smile, zhuangzunv, ornaments, jewelry, headwear, beautiful embroidery, floral print, marvelous design, ancient Chinese traditional clothing'},
    {'name': '欧式田野风(European fields)',
     'img': './style_image/European_fields.jpg',
     'model_id': 'iotang/lora_testing',
     'revision': 'v5',
     'bin_file': 'edgEuropean_Vintage.safetensors',
     'multiplier_style': 0.55,
     'multiplier_human': 0.95,
     'add_prompt_style': '(masterpiece, ultra high res face, face ultra zoom, highres, best quality, ultra detailed, detailed background, cinematic lighting, portrait:1.2), sfw, focused, edgEV, wearing edgEV_vintage dress, field, natural lighting, windy hair, gentle hair, clean'},
    {'name': '雪山羽绒服风(Jacket in Snow Mountain)',
     'img': './style_image/Jacket_in_Snow_Mountain.jpg',
     'model_id': 'iotang/lora_testing',
     'revision': 'v7',
     'bin_file': 'puffy_jacket-1.0.safetensors',
     'multiplier_style': 0.6,
     'multiplier_human': 0.9,
     'add_prompt_style': 'close-up, fur collar, ((jacket)), shirt, pants, winter, (bright sunny day, snow mountain, alpine slopes, snow), gyaru, fashion, trendy, gentle hair'},
    {'name': '漫游宇航员(Roaming Astronaut)',
     'img': './style_image/Roaming_Astronaut.png',
     'model_id':'idlepiggy/zju_16FC',
     'revision': 'v2.0',
     'bin_file': 'firmamentV2.1.safetensors',
     'multiplier_style': 0.7,
     'multiplier_human': 0.9,
     'add_prompt_style': 'firmament,space_helmet,background is universe with stars,moon,looking at viewer'},
    {'name': '复古军装风(Retro military uniform)',
     'img': './style_image/jun_zhuang.png',
     'model_id': 'idlepiggy/zju_16FC',
     'revision': 'v2.0',
     'bin_file': 'minguojunzhuangv1.0.safetensors',
     'multiplier_style': 0.65,
     'multiplier_human': 0.9,
     'add_prompt_style': 'fall, wall behind, blurry, blurry background, depth of field, gloves, hat,  realistic, solo, uniform, black hair, long sleeves, black gloves, cape, military, black headwear, military uniform, peaked cap, military hat, outfit, looking at viewer,front view'},
    {'name': '海港船长风(Sea Captain)',
     'img': './style_image/hai_feng.jpg',
     'model_id': 'idlepiggy/zju_16FC',
     'revision': 'v2.0',
     'bin_file': 'uniform11.safetensors',
     'multiplier_style': 0.75,
     'multiplier_human': 0.9,
     'add_prompt_style': 'Professional,ultra-fine painting,black hair,standing,outdoors,uniform11,police uniform,hat,cloud,sky,seaside background,looking at viewer,slim body with large breast',
     'add_neg_prompt':'hand'},
]

pose_models = [
    {'name': '无姿态控制(No pose control)'},
    {'name': 'pose-v1.1-with-depth'},
    {'name': 'pose-v1.1'}
]

pose_examples = {
    'man': [
        ['./poses/man/pose1.png'],
        ['./poses/man/pose2.png'],
        ['./poses/man/pose3.png'],
        ['./poses/man/pose4.png']
    ],
    'woman': [
        ['./poses/woman/pose1.png'],
        ['./poses/woman/pose2.png'],
        ['./poses/woman/pose3.png'],
        ['./poses/woman/pose4.png'],
    ]
}
