from github import Github, Auth
import json

class App():
    def __init__(self, debugging: bool = False):
        self.debugging = debugging

        self.update_data()

        self.display_top_languages_line_count(10)
        print()
        self.display_top_languages_character_count(10)

    def display_top_languages_line_count(self, entries:int = 5):
        total_lines = 0

        self.__debugging_statement(f"{self.file_types = }")

        for language in self.file_types:
            total_lines += self.file_types[language][0]

        self.__debugging_statement(f"{total_lines = }")

        sorted_languages = sorted(self.file_types, key=lambda x: self.file_types[x][0], reverse=True)

        self.__debugging_statement(f"{sorted_languages = }")

        print("\033[1mTop Languages (By Line Count):\033[0m")

        for i in range(entries):
            print(f"{f"\033[1mLanguage {i+1}":<{(15+len(str(entries)))}}-\033[0m {sorted_languages[i]:^8} - {f"{self.file_types[sorted_languages[i]][0]:,} lines":^25}-{f"{self.file_types[sorted_languages[i]][0] / total_lines * 100 :.2f}%":>7}")

    def display_top_languages_character_count(self, entries:int = 5):
        total_characters = 0

        self.__debugging_statement(f"{self.file_types = }")

        for language in self.file_types:
            total_characters += self.file_types[language][1]

        self.__debugging_statement(f"{total_characters = }")

        sorted_languages = sorted(self.file_types, key=lambda x: self.file_types[x][1], reverse=True)

        self.__debugging_statement(f"{sorted_languages = }")

        print("\033[1mTop Languages (By Character Count):\033[0m")

        for i in range(entries):
            print(f"{f"\033[1mLanguage {i+1}":<{(15+len(str(entries)))}}-\033[0m {sorted_languages[i]:^8} - {f"{self.file_types[sorted_languages[i]][1]:,} characters":^25}-{f"{self.file_types[sorted_languages[i]][1] / total_characters * 100 :.2f}%":>7}")

    def update_data(self):
        with open("tokens.json", "r") as file:
            access_token = json.load(file)["token"]

        self.__debugging_statement(f"{access_token = }")

        auth = Auth.Token(access_token)

        self.git_con = Github(auth=auth)

        repos = self.__get_repos()

        #files = self.__get_repo_files(repos)

        # SAMPLE DATA - 
        files = {'0 - akils CAESAR SYPHUR.py': ['.py', [117, 3393]], '1 - Programming Practice Booklet Students.docx': ['.docx', [0, 0]], '2 - books.bin': ['.bin', [15, 83]], '3 - names.txt': ['.txt', [10, 63]], '4 - Task 37.py': ['.py', [15, 264]], '5 - Task 38.py': ['.py', [16, 279]], '6 - Task 39.py': ['.py', [11, 179]], '7 - Task 40.py': ['.py', [37, 765]], '8 - Task 41.py': ['.py', [19, 558]], '9 - Task 42.py': ['.py', [37, 679]], '10 - Task 43.py': ['.py', [17, 333]], '11 - Task 44.py': ['.py', [10, 225]], '12 - Task 45.py': ['.py', [21, 344]], '13 - Task 46.py': ['.py', [21, 436]], '14 - Task 47.py': ['.py', [23, 505]], '15 - Task 48.py': ['.py', [17, 295]], '16 - Task 49.py': ['.py', [7, 200]], '17 - Task 50.py': ['.py', [56, 1286]], '18 - Task 51.py': ['.py', [34, 689]], '19 - Task 52.py': ['.py', [7, 103]], '20 - Task 53.py': ['.py', [15, 250]], '21 - Task 54.py': ['.py', [11, 237]], '22 - Task 55.py': ['.py', [17, 257]], '23 - Task 56.py': ['.py', [19, 343]], '24 - Task 57.py': ['.py', [6, 158]], '25 - Task 58.py': ['.py', [36, 1070]], '26 - Task 59.py': ['.py', [17, 406]], '27 - Task 61.py': ['.py', [16, 362]], '28 - Task 62.py': ['.py', [14, 428]], '29 - Task 63.py': ['.py', [16, 294]], '30 - Task 1.py': ['.py', [1, 20]], '31 - Task 10.py': ['.py', [6, 131]], '32 - Task 11.py': ['.py', [8, 193]], '33 - Task 12.py': ['.py', [8, 248]], '34 - Task 2.py': ['.py', [6, 137]], '35 - Task 3.py': ['.py', [1, 46]], '36 - Task 4.py': ['.py', [3, 48]], '37 - Task 5.py': ['.py', [7, 97]], '38 - Task 6.py': ['.py', [4, 59]], '39 - Task 7.py': ['.py', [6, 126]], '40 - Task 8.py': ['.py', [8, 196]], '41 - Task 9.py': ['.py', [15, 430]], '42 - Task 13.py': ['.py', [7, 193]], '43 - Task 14.py': ['.py', [12, 345]], '44 - Task 15.py': ['.py', [10, 219]], '45 - Task 16.py': ['.py', [16, 457]], '46 - Task 17.py': ['.py', [40, 857]], '47 - Task 18.py': ['.py', [4, 59]], '48 - Task 19.py': ['.py', [3, 89]], '49 - Task 20.py': ['.py', [19, 319]], '50 - Task 21.py': ['.py', [4, 47]], '51 - Task 22.py': ['.py', [18, 501]], '52 - Task 23.py': ['.py', [8, 116]], '53 - Task 24.py': ['.py', [16, 455]], '54 - Task 25.py': ['.py', [5, 139]], '55 - Task 26.py': ['.py', [3, 95]], '56 - Task 27.py': ['.py', [20, 555]], '57 - Task 28.py': ['.py', [6, 127]], '58 - Task 29.py': ['.py', [10, 298]], '59 - Task 30.py': ['.py', [22, 908]], '60 - Task 31.py': ['.py', [4, 205]], '61 - Task 32.py': ['.py', [42, 1049]], '62 - Task 33.py': ['.py', [11, 327]], '63 - Task 34.py': ['.py', [10, 260]], '64 - Task 35.py': ['.py', [10, 224]], '65 - Task 36.py': ['.py', [18, 400]], '66 - PythonATC.py': ['.py', [113, 4180]], '67 - Plane.png': ['.png', [0, 0]], '68 - Map.png': ['.png', [0, 0]], '69 - backend.py': ['.py', [55, 2041]], '70 - main.py': ['.py', [1, 14]], '71 - Functionality.py': ['.py', [30, 537]], '72 - README.md': ['.md', [24, 778]], '73 - Test.py': ['.py', [13, 245]], '74 - UI.py': ['.py', [104, 3017]], '75 - Functionality.cpython-313.pyc': ['.pyc', [0, 0]], '76 - Functionality.cpython-314.pyc': ['.pyc', [0, 0]], '77 - 2019.pdf': ['.pdf', [0, 0]], '78 - 1a.py': ['.py', [45, 1201]], '79 - 1a.py': ['.py', [17, 356]], '80 - 1a (efficient).py': ['.py', [43, 1104]], '81 - 1a.py': ['.py', [29, 564]], '82 - 2a.py': ['.py', [89, 1777]], '83 - functions.py': ['.py', [43, 1557]], '84 - functionstest.py': ['.py', [62, 1601]], '85 - ui.py': ['.py', [0, 0]], '86 - functions.cpython-314.pyc': ['.pyc', [0, 0]], '87 - README.txt': ['.txt', [3, 29]], '88 - Ticket.pdf': ['.pdf', [0, 0]], '89 - adminSettings.json': ['.json', [3, 25]], '90 - app.py': ['.py', [313, 12035]], '91 - backend.py': ['.py', [766, 29252]], '92 - settings.json': ['.json', [11, 163]], '93 - backend.cpython-314.pyc': ['.pyc', [0, 0]], '94 - admin-dashboard.html': ['.html', [96, 5304]], '95 - admin-pending.html': ['.html', [77, 4162]], '96 - admin-users.html': ['.html', [156, 7891]], '97 - admin-view-user-bookings.html': ['.html', [172, 9781]], '98 - admin-view-user.html': ['.html', [409, 24056]], '99 - dashboard.css': ['.css', [117, 1677]], '100 - pending.css': ['.css', [40, 491]], '101 - style.css': ['.css', [151, 2251]], '102 - users.css': ['.css', [287, 3908]], '103 - view-user-bookings.css': ['.css', [279, 3993]], '104 - view-user.css': ['.css', [709, 10001]], '105 - barcode.png': ['.png', [0, 0]], '106 - date_back.png': ['.png', [0, 0]], '107 - date_forward.png': ['.png', [0, 0]], '108 - delete.png': ['.png', [0, 0]], '109 - edit.webp': ['.webp', [0, 0]], '110 - favicon.ico': ['.ico', [0, 0]], '111 - plus.png': ['.png', [0, 0]], '112 - dashboard.js': ['.js', [21, 674]], '113 - userBookings.js': ['.js', [42, 1415]], '114 - users.js': ['.js', [9, 246]], '115 - viewUser.js': ['.js', [112, 3121]], '116 - 1.jpg': ['.jpg', [0, 0]], '117 - 1.webp': ['.webp', [0, 0]], '118 - 2.jpg': ['.jpg', [0, 0]], '119 - 2.webp': ['.webp', [0, 0]], '120 - none.jpg': ['.jpg', [0, 0]], '121 - 1.webp': ['.webp', [0, 0]], '122 - none.webp': ['.webp', [0, 0]], '123 - functions.py': ['.py', [0, 0]], '124 - game.py': ['.py', [164, 5542]], '125 - backbg.png': ['.png', [0, 0]], '126 - dino.png': ['.png', [0, 0]], '127 - fly.png': ['.png', [0, 0]], '128 - frontbg.png': ['.png', [0, 0]], '129 - obs1.png': ['.png', [0, 0]], '130 - obs2.png': ['.png', [0, 0]], '131 - functions.cpython-312.pyc': ['.pyc', [0, 0]], '132 - functions.cpython-314.pyc': ['.pyc', [0, 0]], '133 - backend.py': ['.py', [120, 4018]], '134 - database.db': ['.db', [0, 0]], '135 - main.py': ['.py', [31, 717]], '136 - backend.cpython-314.pyc': ['.pyc', [0, 0]], '137 - rippedQuestionPapers.txt': ['.txt', [5, 74]], '138 - index.html': ['.html', [51, 4760]], '139 - Correct.mp3': ['.mp3', [0, 0]], '140 - Incorrect.mp3': ['.mp3', [0, 0]], '141 - style.css': ['.css', [179, 2448]], '142 - favicon.ico': ['.ico', [0, 0]], '143 - functions.js': ['.js', [120, 4172]], '144 - 10.jpeg': ['.jpeg', [0, 0]], '145 - 13.jpeg': ['.jpeg', [0, 0]], '146 - 17.jpeg': ['.jpeg', [0, 0]], '147 - 19.jpeg': ['.jpeg', [0, 0]], '148 - 3.jpeg': ['.jpeg', [0, 0]], '149 - download.jpeg': ['.jpeg', [0, 0]], '150 - Economy_Simulator_Proof_of_Concept.py': ['.py', [111, 4597]], '151 - Fitness.py': ['.py', [177, 5744]], '152 - Test.sln': ['.sln', [23, 953]], '153 - Test.py': ['.py', [17, 367]], '154 - Test.pyproj': ['.pyproj', [35, 1512]], '155 - .gitignore': ['.gitignore', [11, 200]], '156 - main.py': ['.py', [113, 18736]], '157 - tokens.json': ['.json', [3, 29]], '158 - Learning-C-.sln': ['.sln', [24, 1080]], '159 - Programming Practice Booklet Students.pdf': ['.pdf', [0, 0]], '160 - App.csproj': ['.csproj', [10, 241]], '161 - Program.cs': ['.cs', [12, 270]], '162 - Task 1.cs': ['.cs', [9, 159]], '163 - Task 10.cs': ['.cs', [36, 1325]], '164 - Task 11.cs': ['.cs', [50, 1943]], '165 - Task 12.cs': ['.cs', [23, 797]], '166 - Task 13.cs': ['.cs', [31, 927]], '167 - Task 14.cs': ['.cs', [43, 1604]], '168 - Task 15.cs': ['.cs', [28, 935]], '169 - Task 16.cs': ['.cs', [43, 1321]], '170 - Task 17.cs': ['.cs', [68, 2033]], '171 - Task 18.cs': ['.cs', [15, 293]], '172 - Task 19.cs': ['.cs', [16, 454]], '173 - Task 2.cs': ['.cs', [14, 363]], '174 - Task 20.cs': ['.cs', [40, 1154]], '175 - Task 21.cs': ['.cs', [16, 296]], '176 - Task 22.cs': ['.cs', [40, 1228]], '177 - Task 23.cs': ['.cs', [13, 283]], '178 - Task 24.cs': ['.cs', [48, 1420]], '179 - Task 3.cs': ['.cs', [9, 257]], '180 - Task 4.cs': ['.cs', [11, 312]], '181 - Task 5.cs': ['.cs', [36, 1020]], '182 - Task 6.cs': ['.cs', [28, 713]], '183 - Task 7.cs': ['.cs', [29, 837]], '184 - Task 8.cs': ['.cs', [29, 942]], '185 - Task 9.cs': ['.cs', [34, 1318]], '186 - App.csproj.nuget.dgspec.json': ['.json', [341, 21022]], '187 - App.csproj.nuget.g.props': ['.props', [15, 1119]], '188 - App.csproj.nuget.g.targets': ['.targets', [2, 147]], '189 - project.assets.json': ['.json', [346, 20380]], '190 - project.nuget.cache': ['.cache', [8, 199]], '191 - App.deps.json': ['.json', [23, 381]], '192 - App.dll': ['.dll', [0, 0]], '193 - App.exe': ['.exe', [0, 0]], '194 - App.pdb': ['.pdb', [0, 0]], '195 - App.runtimeconfig.json': ['.json', [12, 259]], '196 - .NETCoreApp,Version=v10.0.AssemblyAttributes.cs': ['.cs', [4, 196]], '197 - App.AssemblyInfo.cs': ['.cs', [22, 961]], '198 - App.AssemblyInfoInputs.cache': ['.cache', [1, 65]], '199 - App.GeneratedMSBuildEditorConfig.editorconfig': ['.editorconfig', [17, 768]], '200 - App.GlobalUsings.g.cs': ['.cs', [8, 231]], '201 - App.assets.cache': ['.cache', [0, 0]], '202 - App.csproj.CoreCompileInputs.cache': ['.cache', [1, 65]], '203 - App.csproj.FileListAbsolute.txt': ['.txt', [15, 1241]], '204 - App.dll': ['.dll', [0, 0]], '205 - App.genruntimeconfig.cache': ['.cache', [1, 65]], '206 - App.pdb': ['.pdb', [0, 0]], '207 - App.sourcelink.json': ['.json', [1, 172]], '208 - apphost.exe': ['.exe', [0, 0]], '209 - App.dll': ['.dll', [0, 0]], '210 - App.dll': ['.dll', [0, 0]], '211 - .gitattributes': ['.gitattributes', [63, 2518]], '212 - .gitignore': ['.gitignore', [364, 6230]], '213 - FinalList.txt': ['.txt', [0, 0]], '214 - FullList.txt': ['.txt', [3, 21]], '215 - List Ranking App.pyproj': ['.pyproj', [35, 1560]], '216 - List_Ranking_App.py': ['.py', [76, 2312]], '217 - LongList.txt': ['.txt', [3, 23]], '218 - ShortList.txt': ['.txt', [0, 0]], '219 - filePaths.json': ['.json', [6, 193]], '220 - launcher.pyw': ['.pyw', [53, 1707]], '221 - settings.json': ['.json', [6, 73]], '222 - MSFS Companion.py': ['.py', [336, 13265]], '223 - README.md': ['.md', [35, 1805]], '224 - Flight_Sim_Snapshots.py': ['.py', [37, 1135]], '225 - Functions.py': ['.py', [40, 1345]], '226 - Test.py': ['.py', [12, 250]], '227 - README': ['.README', [1, 151]], '228 - Encryption Tool.lnk': ['.lnk', [0, 0]], '229 - README.md': ['.md', [63, 7159]], '230 - settings.json': ['.json', [5, 48]], '231 - Encryption Test.py': ['.py', [60, 1825]], '232 - Encryption.py': ['.py', [188, 6294]], '233 - RSAEncryption.py': ['.py', [85, 3628]], '234 - UI.py': ['.py', [519, 28291]], '235 - UI.pyw': ['.pyw', [519, 28291]], '236 - Encryption.cpython-314.pyc': ['.pyc', [0, 0]], '237 - RSAEncryption.cpython-314.pyc': ['.pyc', [0, 0]], '238 - Task 1.py': ['.py', [39, 1120]], '239 - Task 2.py': ['.py', [56, 1265]], '240 - Task 1.py': ['.py', [53, 1618]], '241 - Task 2.py': ['.py', [24, 586]], '242 - functions.py': ['.py', [0, 0]], '243 - ui.py': ['.py', [216, 8059]], '244 - words_alpha.txt': ['.txt', [0, 0]], '245 - functions.cpython-314.pyc': ['.pyc', [0, 0]], '246 - functions.py': ['.py', [28, 849]], '247 - ui.py': ['.py', [136, 4784]], '248 - users.db': ['.db', [0, 0]], '249 - functions.cpython-314.pyc': ['.pyc', [0, 0]], '250 - 404.html': ['.html', [12, 255]], '251 - CNAME': ['.CNAME', [1, 14]], '252 - about.html': ['.html', [119, 16745]], '253 - articles-overviews.html': ['.html', [56, 3102]], '254 - contact.html': ['.html', [56, 3127]], '255 - freelance.html': ['.html', [56, 3107]], '256 - index.html': ['.html', [56, 3543]], '257 - portfolio.html': ['.html', [56, 3125]], '258 - about.css': ['.css', [88, 1358]], '259 - style.css': ['.css', [151, 2234]], '260 - 152-cockpit.jpg': ['.jpg', [0, 0]], '261 - 152-landscape.jpg': ['.jpg', [0, 0]], '262 - about-mug.jpg': ['.jpg', [0, 0]], '263 - croatia-landscape.jpg': ['.jpg', [0, 0]], '264 - favicon.ico': ['.ico', [0, 0]], '265 - menu.svg': ['.svg', [1, 193]], '266 - script.js': ['.js', [44, 1290]], '267 - Revise.sln': ['.sln', [23, 958]], '268 - Revise.py': ['.py', [29, 645]], '269 - Revise.pyproj': ['.pyproj', [35, 1521]], '270 - Revise.pyw': ['.pyw', [29, 645]], '271 - Revise.pyw - Shortcut.lnk': ['.lnk', [0, 0]], '272 - Correct.mp3': ['.mp3', [0, 0]], '273 - Incorrect.mp3': ['.mp3', [0, 0]], '274 - Questions.db': ['.db', [0, 0]], '275 - Questions.py': ['.py', [729, 28113]], '276 - buttons.py': ['.py', [27, 705]], '277 - functionality.py': ['.py', [45, 1210]], '278 - ui.py': ['.py', [35, 1342]], '279 - buttons.cpython-314.pyc': ['.pyc', [0, 0]], '280 - functionality.cpython-314.pyc': ['.pyc', [0, 0]], '281 - main.pyw': ['.pyw', [99, 3421]], '282 - To Do List.sln': ['.sln', [23, 971]], '283 - To Do List.pyproj': ['.pyproj', [35, 1536]], '284 - ToDo.db': ['.db', [0, 0]], '285 - To_Do_List.py': ['.py', [598, 31420]], '286 - mono.json': ['.json', [155, 4951]], '287 - bridge.py': ['.py', [61, 2038]], '288 - discordSettings.json': ['.json', [4, 132]], '289 - items.json': ['.json', [28, 1579]], '290 - notifications.py': ['.py', [80, 3120]], '291 - pulled.db': ['.db', [0, 0]], '292 - scraper.py': ['.py', [360, 13464]], '293 - test.py': ['.py', [36, 881]], '294 - usersettings.json': ['.json', [3, 39]], '295 - notifications.cpython-313.pyc': ['.pyc', [0, 0]], '296 - notifications.cpython-314.pyc': ['.pyc', [0, 0]], '297 - scraper.cpython-313.pyc': ['.pyc', [0, 0]], '298 - scraper.cpython-314.pyc': ['.pyc', [0, 0]], '299 - Image0.webp': ['.webp', [0, 0]], '300 - Image1.webp': ['.webp', [0, 0]], '301 - Image2.webp': ['.webp', [0, 0]], '302 - Image3.webp': ['.webp', [0, 0]], '303 - Image4.webp': ['.webp', [0, 0]], '304 - Climate-S006-001(in).csv': ['.csv', [121, 14926]], '305 - app.py': ['.py', [81, 4416]], '306 - backend.py': ['.py', [21, 783]], '307 - untitled.ui': ['.ui', [217, 4599]], '308 - untitled_ui.py': ['.py', [97, 5239]], '309 - settings.json': ['.json', [5, 48]], '310 - backend.cpython-314.pyc': ['.pyc', [0, 0]], '311 - maxTemp.jpg': ['.jpg', [0, 0]], '312 - meanTemp.jpg': ['.jpg', [0, 0]], '313 - minTemp.jpg': ['.jpg', [0, 0]], '314 - rain.jpg': ['.jpg', [0, 0]], '315 - Climate-S006-001(in).csv': ['.csv', [121, 15047]], '316 - app.py': ['.py', [56, 2898]], '317 - backend.py': ['.py', [41, 1650]], '318 - settings.json': ['.json', [5, 49]], '319 - backend.cpython-314.pyc': ['.pyc', [0, 0]], '320 - index.html': ['.html', [59, 2948]], '321 - style.css': ['.css', [100, 1409]], '322 - favicon.ico': ['.ico', [0, 0]], '323 - maxTemp.jpg': ['.jpg', [0, 0]], '324 - meanTemp.jpg': ['.jpg', [0, 0]], '325 - minTemp.jpg': ['.jpg', [0, 0]], '326 - rain.jpg': ['.jpg', [0, 0]], '327 - Word_Processor___Text_Document_Revision_GCSE_Computer_Science.py': ['.py', [79, 2615]], '328 - README.md': ['.md', [51, 1770]], '329 - Correct.mp3': ['.mp3', [0, 0]], '330 - Incorrect.mp3': ['.mp3', [0, 0]], '331 - SongGuesser.py': ['.py', [553, 27800]], '332 - Songs.db': ['.db', [0, 0]], '333 - Users.db': ['.db', [0, 0]], '334 - Aud.mp3': ['.mp3', [0, 0]], '335 - Cvr.png': ['.png', [0, 0]], '336 - Aud.mp3': ['.mp3', [0, 0]], '337 - Cvr.png': ['.png', [0, 0]], '338 - Aud.mp3': ['.mp3', [0, 0]], '339 - Cvr.png': ['.png', [0, 0]], '340 - Aud.mp3': ['.mp3', [0, 0]], '341 - Cvr.png': ['.png', [0, 0]], '342 - Aud.mp3': ['.mp3', [0, 0]], '343 - Cvr.png': ['.png', [0, 0]], '344 - untitled.mp3': ['.mp3', [0, 0]], '345 - Aud.mp3': ['.mp3', [0, 0]], '346 - Cvr.png': ['.png', [0, 0]], '347 - Aud.mp3': ['.mp3', [0, 0]], '348 - Cvr.png': ['.png', [0, 0]], '349 - Aud.mp3': ['.mp3', [0, 0]], '350 - Cvr.png': ['.png', [0, 0]], '351 - Aud.mp3': ['.mp3', [0, 0]], '352 - Cvr.png': ['.png', [0, 0]], '353 - Aud.mp3': ['.mp3', [0, 0]], '354 - Cvr.png': ['.png', [0, 0]], '355 - Aud.mp3': ['.mp3', [0, 0]], '356 - Cvr.png': ['.png', [0, 0]], '357 - Aud.mp3': ['.mp3', [0, 0]], '358 - Cvr.png': ['.png', [0, 0]], '359 - Aud.mp3': ['.mp3', [0, 0]], '360 - Cvr.png': ['.png', [0, 0]], '361 - Aud.mp3': ['.mp3', [0, 0]], '362 - Cvr.png': ['.png', [0, 0]], '363 - Aud.mp3': ['.mp3', [0, 0]], '364 - Cvr.png': ['.png', [0, 0]], '365 - Aud.mp3': ['.mp3', [0, 0]], '366 - Cvr.png': ['.png', [0, 0]], '367 - Aud.mp3': ['.mp3', [0, 0]], '368 - Cvr.png': ['.png', [0, 0]], '369 - Aud.mp3': ['.mp3', [0, 0]], '370 - Cvr.png': ['.png', [0, 0]], '371 - Aud.mp3': ['.mp3', [0, 0]], '372 - Cvr.png': ['.png', [0, 0]], '373 - Aud.mp3': ['.mp3', [0, 0]], '374 - Cvr.png': ['.png', [0, 0]], '375 - Aud.mp3': ['.mp3', [0, 0]], '376 - Cvr.png': ['.png', [0, 0]], '377 - Aud.mp3': ['.mp3', [0, 0]], '378 - Cvr.png': ['.png', [0, 0]], '379 - Aud.mp3': ['.mp3', [0, 0]], '380 - Cvr.png': ['.png', [0, 0]], '381 - Aud.mp3': ['.mp3', [0, 0]], '382 - Cvr.png': ['.png', [0, 0]], '383 - Aud.mp3': ['.mp3', [0, 0]], '384 - Cvr.png': ['.png', [0, 0]], '385 - Aud.mp3': ['.mp3', [0, 0]], '386 - Cvr.png': ['.png', [0, 0]], '387 - Aud.mp3': ['.mp3', [0, 0]], '388 - Cvr.png': ['.png', [0, 0]], '389 - Aud.mp3': ['.mp3', [0, 0]], '390 - Cvr.png': ['.png', [0, 0]], '391 - Aud.mp3': ['.mp3', [0, 0]], '392 - Cvr.png': ['.png', [0, 0]], '393 - Aud.mp3': ['.mp3', [0, 0]], '394 - Cvr.png': ['.png', [0, 0]], '395 - Aud.mp3': ['.mp3', [0, 0]], '396 - Cvr.png': ['.png', [0, 0]], '397 - Aud.mp3': ['.mp3', [0, 0]], '398 - Cvr.png': ['.png', [0, 0]], '399 - Aud.mp3': ['.mp3', [0, 0]], '400 - Cvr.png': ['.png', [0, 0]], '401 - Aud.mp3': ['.mp3', [0, 0]], '402 - Cvr.png': ['.png', [0, 0]], '403 - Aud.mp3': ['.mp3', [0, 0]], '404 - Cvr.png': ['.png', [0, 0]], '405 - Aud.mp3': ['.mp3', [0, 0]], '406 - Cvr.png': ['.png', [0, 0]], '407 - Aud.mp3': ['.mp3', [0, 0]], '408 - Cvr.png': ['.png', [0, 0]], '409 - Aud.mp3': ['.mp3', [0, 0]], '410 - Cvr.png': ['.png', [0, 0]], '411 - Aud.mp3': ['.mp3', [0, 0]], '412 - Cvr.png': ['.png', [0, 0]], '413 - Aud.mp3': ['.mp3', [0, 0]], '414 - Cvr.png': ['.png', [0, 0]], '415 - Aud.mp3': ['.mp3', [0, 0]], '416 - Cvr.png': ['.png', [0, 0]], '417 - Aud.mp3': ['.mp3', [0, 0]], '418 - Cvr.png': ['.png', [0, 0]], '419 - README.md': ['.md', [17, 756]], '420 - DLC #1.pyproj': ['.pyproj', [35, 1520]], '421 - DLC__1.py': ['.py', [80, 2862]], '422 - Songs.db': ['.db', [0, 0]], '423 - Aud.mp3': ['.mp3', [0, 0]], '424 - Cvr.png': ['.png', [0, 0]], '425 - Aud.mp3': ['.mp3', [0, 0]], '426 - Cvr.png': ['.png', [0, 0]], '427 - Aud.mp3': ['.mp3', [0, 0]], '428 - Cvr.png': ['.png', [0, 0]], '429 - Aud.mp3': ['.mp3', [0, 0]], '430 - Cvr.png': ['.png', [0, 0]], '431 - Aud.mp3': ['.mp3', [0, 0]], '432 - Cvr.png': ['.png', [0, 0]], '433 - Aud.mp3': ['.mp3', [0, 0]], '434 - Cvr.png': ['.png', [0, 0]], '435 - Aud.mp3': ['.mp3', [0, 0]], '436 - Cvr.png': ['.png', [0, 0]], '437 - Aud.mp3': ['.mp3', [0, 0]], '438 - Cvr.png': ['.png', [0, 0]], '439 - Aud.mp3': ['.mp3', [0, 0]], '440 - Cvr.png': ['.png', [0, 0]], '441 - Aud.mp3': ['.mp3', [0, 0]], '442 - Cvr.png': ['.png', [0, 0]], '443 - README.md': ['.md', [2, 444]], '444 - Mod Loader.py': ['.py', [80, 2862]], '445 - Songs.db': ['.db', [0, 0]]}

        self.__debugging_statement(f"{files = }")
        self.__debugging_statement(f"{len(files) = }")

        self.file_types = {}

        for file in files:
            if files[file][0] in self.file_types:
                self.file_types[files[file][0]][0] += files[file][1][0]
                self.file_types[files[file][0]][1] += files[file][1][1]
            else:
                self.file_types[files[file][0]] = [files[file][1][0], files[file][1][1]]

    def __get_repos(self):
        user = self.git_con.get_user()
        repos = user.get_repos(visibility="all")

        print(f"{repos.totalCount} Repos Found")

        repo_names = [repo.name for repo in repos]

        for i in range(len(repo_names)):
            self.__debugging_statement(f"{i+1} - {repos[i]}")

        return repos
    
    def __get_repo_files(self, repos):
        files = {}

        index = 1
        file_index = 0

        for repo in repos:
            print(f"Working on repo no. {index} ({repo.name})...")
            index += 1

            repo_files = []
            contents: list = repo.get_contents("")

            while len(contents) > 0:
                element = contents.pop(0)

                self.__debugging_statement(f"{element = }")

                if element.type == "dir": # Is folder
                    contents.extend(repo.get_contents(element.path))
                    self.__debugging_statement("\033[95mElement is directory\033[0m")
                else:
                    try: # for if it is a single file in directory or list
                        repo_files.extend(element)
                    except:
                        repo_files.extend([element])

                    self.__debugging_statement(f"{repo_files = }")

                self.__debugging_statement()

            self.__debugging_statement(f"\033[92m{repo_files = }\033[0m")

            for file in repo_files:
                file_title = file.name
                
                file_title_split = file_title.split(".")
                file_type = f".{file_title_split[-1]}"

                self.__debugging_statement(f"{file_title = }")
                self.__debugging_statement(f"{file_type = }")

                try:
                    file_content = file.decoded_content.decode("utf-8")
                except: # for unsupported file types
                    file_content = ""

                line_count = len(file_content.splitlines())
                character_count = len(file_content)

                self.__debugging_statement(f"{line_count = }")
                self.__debugging_statement(f"{character_count = }")

                files[f"{file_index} - {file_title}"] = [file_type, [line_count, character_count]]

                file_index += 1

        return files
    
    def __debugging_statement(self, message = ""):
        if self.debugging:
            if message != "":
                print(f"\033[94mDEBUGGING - {message}\033[0m")
            else:
                print()

if __name__ == "__main__":
    app = App(debugging=False)