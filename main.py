from github import Github, Auth
import json

class App():
    def __init__(self, debugging: bool = False):
        self.debugging = debugging

        with open("tokens.json", "r") as file:
            access_token = json.load(file)["token"]

        self.__debugging_statement(f"{access_token = }")

        auth = Auth.Token(access_token)

        self.git_con = Github(auth=auth)

        repos = self.__get_repos()

        files = self.__get_repo_files(repos)
        # SAMPLE DATA - files = {'0 - akils CAESAR SYPHUR.py': ['.py', 117], '1 - Programming Practice Booklet Students.docx': ['.docx', 0], '2 - books.bin': ['.bin', 15], '3 - names.txt': ['.txt', 10], '4 - Task 37.py': ['.py', 15], '5 - Task 38.py': ['.py', 16], '6 - Task 39.py': ['.py', 11], '7 - Task 40.py': ['.py', 37], '8 - Task 41.py': ['.py', 19], '9 - Task 42.py': ['.py', 37], '10 - Task 43.py': ['.py', 17], '11 - Task 44.py': ['.py', 10], '12 - Task 45.py': ['.py', 21], '13 - Task 46.py': ['.py', 21], '14 - Task 47.py': ['.py', 23], '15 - Task 48.py': ['.py', 17], '16 - Task 49.py': ['.py', 7], '17 - Task 50.py': ['.py', 56], '18 - Task 51.py': ['.py', 34], '19 - Task 52.py': ['.py', 7], '20 - Task 53.py': ['.py', 15], '21 - Task 54.py': ['.py', 11], '22 - Task 55.py': ['.py', 17], '23 - Task 56.py': ['.py', 19], '24 - Task 57.py': ['.py', 6], '25 - Task 58.py': ['.py', 36], '26 - Task 59.py': ['.py', 17], '27 - Task 61.py': ['.py', 16], '28 - Task 62.py': ['.py', 14], '29 - Task 63.py': ['.py', 16], '30 - Task 1.py': ['.py', 1], '31 - Task 10.py': ['.py', 6], '32 - Task 11.py': ['.py', 8], '33 - Task 12.py': ['.py', 8], '34 - Task 2.py': ['.py', 6], '35 - Task 3.py': ['.py', 1], '36 - Task 4.py': ['.py', 3], '37 - Task 5.py': ['.py', 7], '38 - Task 6.py': ['.py', 4], '39 - Task 7.py': ['.py', 6], '40 - Task 8.py': ['.py', 8], '41 - Task 9.py': ['.py', 15], '42 - Task 13.py': ['.py', 7], '43 - Task 14.py': ['.py', 12], '44 - Task 15.py': ['.py', 10], '45 - Task 16.py': ['.py', 16], '46 - Task 17.py': ['.py', 40], '47 - Task 18.py': ['.py', 4], '48 - Task 19.py': ['.py', 3], '49 - Task 20.py': ['.py', 19], '50 - Task 21.py': ['.py', 4], '51 - Task 22.py': ['.py', 18], '52 - Task 23.py': ['.py', 8], '53 - Task 24.py': ['.py', 16], '54 - Task 25.py': ['.py', 5], '55 - Task 26.py': ['.py', 3], '56 - Task 27.py': ['.py', 20], '57 - Task 28.py': ['.py', 6], '58 - Task 29.py': ['.py', 10], '59 - Task 30.py': ['.py', 22], '60 - Task 31.py': ['.py', 4], '61 - Task 32.py': ['.py', 42], '62 - Task 33.py': ['.py', 11], '63 - Task 34.py': ['.py', 10], '64 - Task 35.py': ['.py', 10], '65 - Task 36.py': ['.py', 18], '66 - PythonATC.py': ['.py', 113], '67 - Plane.png': ['.png', 0], '68 - Map.png': ['.png', 0], '69 - backend.py': ['.py', 55], '70 - main.py': ['.py', 1], '71 - Functionality.py': ['.py', 30], '72 - README.md': ['.md', 24], '73 - Test.py': ['.py', 13], '74 - UI.py': ['.py', 104], '75 - Functionality.cpython-313.pyc': ['.pyc', 0], '76 - Functionality.cpython-314.pyc': ['.pyc', 0], '77 - 2019.pdf': ['.pdf', 0], '78 - 1a.py': ['.py', 45], '79 - 1a.py': ['.py', 17], '80 - 1a (efficient).py': ['.py', 43], '81 - 1a.py': ['.py', 29], '82 - 2a.py': ['.py', 89], '83 - functions.py': ['.py', 43], '84 - functionstest.py': ['.py', 62], '85 - ui.py': ['.py', 0], '86 - functions.cpython-314.pyc': ['.pyc', 0], '87 - README.txt': ['.txt', 3], '88 - Ticket.pdf': ['.pdf', 0], '89 - adminSettings.json': ['.json', 3], '90 - app.py': ['.py', 313], '91 - backend.py': ['.py', 766], '92 - settings.json': ['.json', 11], '93 - backend.cpython-314.pyc': ['.pyc', 0], '94 - admin-dashboard.html': ['.html', 96], '95 - admin-pending.html': ['.html', 77], '96 - admin-users.html': ['.html', 156], '97 - admin-view-user-bookings.html': ['.html', 172], '98 - admin-view-user.html': ['.html', 409], '99 - dashboard.css': ['.css', 117], '100 - pending.css': ['.css', 40], '101 - style.css': ['.css', 151], '102 - users.css': ['.css', 287], '103 - view-user-bookings.css': ['.css', 279], '104 - view-user.css': ['.css', 709], '105 - barcode.png': ['.png', 0], '106 - date_back.png': ['.png', 0], '107 - date_forward.png': ['.png', 0], '108 - delete.png': ['.png', 0], '109 - edit.webp': ['.webp', 0], '110 - favicon.ico': ['.ico', 0], '111 - plus.png': ['.png', 0], '112 - dashboard.js': ['.js', 21], '113 - userBookings.js': ['.js', 42], '114 - users.js': ['.js', 9], '115 - viewUser.js': ['.js', 112], '116 - 1.jpg': ['.jpg', 0], '117 - 1.webp': ['.webp', 0], '118 - 2.jpg': ['.jpg', 0], '119 - 2.webp': ['.webp', 0], '120 - none.jpg': ['.jpg', 0], '121 - 1.webp': ['.webp', 0], '122 - none.webp': ['.webp', 0], '123 - functions.py': ['.py', 0], '124 - game.py': ['.py', 164], '125 - backbg.png': ['.png', 0], '126 - dino.png': ['.png', 0], '127 - fly.png': ['.png', 0], '128 - frontbg.png': ['.png', 0], '129 - obs1.png': ['.png', 0], '130 - obs2.png': ['.png', 0], '131 - functions.cpython-312.pyc': ['.pyc', 0], '132 - functions.cpython-314.pyc': ['.pyc', 0], '133 - backend.py': ['.py', 120], '134 - database.db': ['.db', 0], '135 - main.py': ['.py', 31], '136 - backend.cpython-314.pyc': ['.pyc', 0], '137 - rippedQuestionPapers.txt': ['.txt', 5], '138 - index.html': ['.html', 51], '139 - Correct.mp3': ['.mp3', 0], '140 - Incorrect.mp3': ['.mp3', 0], '141 - style.css': ['.css', 179], '142 - favicon.ico': ['.ico', 0], '143 - functions.js': ['.js', 120], '144 - 10.jpeg': ['.jpeg', 0], '145 - 13.jpeg': ['.jpeg', 0], '146 - 17.jpeg': ['.jpeg', 0], '147 - 19.jpeg': ['.jpeg', 0], '148 - 3.jpeg': ['.jpeg', 0], '149 - download.jpeg': ['.jpeg', 0], '150 - Economy_Simulator_Proof_of_Concept.py': ['.py', 111], '151 - Fitness.py': ['.py', 177], '152 - Test.sln': ['.sln', 23], '153 - Test.py': ['.py', 17], '154 - Test.pyproj': ['.pyproj', 35], '155 - .gitignore': ['.gitignore', 0], '156 - main.py': ['.py', 0], '157 - tokens.json': ['.json', 3], '158 - Learning-C-.sln': ['.sln', 24], '159 - Programming Practice Booklet Students.pdf': ['.pdf', 0], '160 - App.csproj': ['.csproj', 10], '161 - Program.cs': ['.cs', 12], '162 - Task 1.cs': ['.cs', 9], '163 - Task 10.cs': ['.cs', 36], '164 - Task 11.cs': ['.cs', 50], '165 - Task 12.cs': ['.cs', 23], '166 - Task 13.cs': ['.cs', 31], '167 - Task 14.cs': ['.cs', 43], '168 - Task 15.cs': ['.cs', 28], '169 - Task 16.cs': ['.cs', 43], '170 - Task 17.cs': ['.cs', 68], '171 - Task 18.cs': ['.cs', 15], '172 - Task 19.cs': ['.cs', 16], '173 - Task 2.cs': ['.cs', 14], '174 - Task 20.cs': ['.cs', 40], '175 - Task 21.cs': ['.cs', 16], '176 - Task 22.cs': ['.cs', 40], '177 - Task 23.cs': ['.cs', 13], '178 - Task 24.cs': ['.cs', 48], '179 - Task 3.cs': ['.cs', 9], '180 - Task 4.cs': ['.cs', 11], '181 - Task 5.cs': ['.cs', 36], '182 - Task 6.cs': ['.cs', 28], '183 - Task 7.cs': ['.cs', 29], '184 - Task 8.cs': ['.cs', 29], '185 - Task 9.cs': ['.cs', 34], '186 - App.csproj.nuget.dgspec.json': ['.json', 341], '187 - App.csproj.nuget.g.props': ['.props', 15], '188 - App.csproj.nuget.g.targets': ['.targets', 2], '189 - project.assets.json': ['.json', 346], '190 - project.nuget.cache': ['.cache', 8], '191 - App.deps.json': ['.json', 23], '192 - App.dll': ['.dll', 0], '193 - App.exe': ['.exe', 0], '194 - App.pdb': ['.pdb', 0], '195 - App.runtimeconfig.json': ['.json', 12], '196 - .NETCoreApp,Version=v10.0.AssemblyAttributes.cs': ['.cs', 4], '197 - App.AssemblyInfo.cs': ['.cs', 22], '198 - App.AssemblyInfoInputs.cache': ['.cache', 1], '199 - App.GeneratedMSBuildEditorConfig.editorconfig': ['.editorconfig', 17], '200 - App.GlobalUsings.g.cs': ['.cs', 8], '201 - App.assets.cache': ['.cache', 0], '202 - App.csproj.CoreCompileInputs.cache': ['.cache', 1], '203 - App.csproj.FileListAbsolute.txt': ['.txt', 15], '204 - App.dll': ['.dll', 0], '205 - App.genruntimeconfig.cache': ['.cache', 1], '206 - App.pdb': ['.pdb', 0], '207 - App.sourcelink.json': ['.json', 1], '208 - apphost.exe': ['.exe', 0], '209 - App.dll': ['.dll', 0], '210 - App.dll': ['.dll', 0], '211 - .gitattributes': ['.gitattributes', 63], '212 - .gitignore': ['.gitignore', 364], '213 - FinalList.txt': ['.txt', 0], '214 - FullList.txt': ['.txt', 3], '215 - List Ranking App.pyproj': ['.pyproj', 35], '216 - List_Ranking_App.py': ['.py', 76], '217 - LongList.txt': ['.txt', 3], '218 - ShortList.txt': ['.txt', 0], '219 - filePaths.json': ['.json', 6], '220 - launcher.pyw': ['.pyw', 53], '221 - settings.json': ['.json', 6], '222 - MSFS Companion.py': ['.py', 336], '223 - README.md': ['.md', 35], '224 - Flight_Sim_Snapshots.py': ['.py', 37], '225 - Functions.py': ['.py', 40], '226 - Test.py': ['.py', 12], '227 - README': ['.README', 1], '228 - Encryption Tool.lnk': ['.lnk', 0], '229 - README.md': ['.md', 63], '230 - settings.json': ['.json', 5], '231 - Encryption Test.py': ['.py', 60], '232 - Encryption.py': ['.py', 188], '233 - RSAEncryption.py': ['.py', 85], '234 - UI.py': ['.py', 519], '235 - UI.pyw': ['.pyw', 519], '236 - Encryption.cpython-314.pyc': ['.pyc', 0], '237 - RSAEncryption.cpython-314.pyc': ['.pyc', 0], '238 - Task 1.py': ['.py', 39], '239 - Task 2.py': ['.py', 56], '240 - Task 1.py': ['.py', 53], '241 - Task 2.py': ['.py', 24], '242 - functions.py': ['.py', 0], '243 - ui.py': ['.py', 216], '244 - words_alpha.txt': ['.txt', 0], '245 - functions.cpython-314.pyc': ['.pyc', 0], '246 - functions.py': ['.py', 28], '247 - ui.py': ['.py', 136], '248 - users.db': ['.db', 0], '249 - functions.cpython-314.pyc': ['.pyc', 0], '250 - 404.html': ['.html', 12], '251 - CNAME': ['.CNAME', 1], '252 - about.html': ['.html', 119], '253 - articles-overviews.html': ['.html', 56], '254 - contact.html': ['.html', 56], '255 - freelance.html': ['.html', 56], '256 - index.html': ['.html', 56], '257 - portfolio.html': ['.html', 56], '258 - about.css': ['.css', 88], '259 - style.css': ['.css', 151], '260 - 152-cockpit.jpg': ['.jpg', 0], '261 - 152-landscape.jpg': ['.jpg', 0], '262 - about-mug.jpg': ['.jpg', 0], '263 - croatia-landscape.jpg': ['.jpg', 0], '264 - favicon.ico': ['.ico', 0], '265 - menu.svg': ['.svg', 1], '266 - script.js': ['.js', 44], '267 - Revise.sln': ['.sln', 23], '268 - Revise.py': ['.py', 29], '269 - Revise.pyproj': ['.pyproj', 35], '270 - Revise.pyw': ['.pyw', 29], '271 - Revise.pyw - Shortcut.lnk': ['.lnk', 0], '272 - Correct.mp3': ['.mp3', 0], '273 - Incorrect.mp3': ['.mp3', 0], '274 - Questions.db': ['.db', 0], '275 - Questions.py': ['.py', 729], '276 - buttons.py': ['.py', 27], '277 - functionality.py': ['.py', 45], '278 - ui.py': ['.py', 35], '279 - buttons.cpython-314.pyc': ['.pyc', 0], '280 - functionality.cpython-314.pyc': ['.pyc', 0], '281 - main.pyw': ['.pyw', 99], '282 - To Do List.sln': ['.sln', 23], '283 - To Do List.pyproj': ['.pyproj', 35], '284 - ToDo.db': ['.db', 0], '285 - To_Do_List.py': ['.py', 598], '286 - mono.json': ['.json', 155], '287 - bridge.py': ['.py', 61], '288 - discordSettings.json': ['.json', 4], '289 - items.json': ['.json', 28], '290 - notifications.py': ['.py', 80], '291 - pulled.db': ['.db', 0], '292 - scraper.py': ['.py', 360], '293 - test.py': ['.py', 36], '294 - usersettings.json': ['.json', 3], '295 - notifications.cpython-313.pyc': ['.pyc', 0], '296 - notifications.cpython-314.pyc': ['.pyc', 0], '297 - scraper.cpython-313.pyc': ['.pyc', 0], '298 - scraper.cpython-314.pyc': ['.pyc', 0], '299 - Image0.webp': ['.webp', 0], '300 - Image1.webp': ['.webp', 0], '301 - Image2.webp': ['.webp', 0], '302 - Image3.webp': ['.webp', 0], '303 - Image4.webp': ['.webp', 0], '304 - Climate-S006-001(in).csv': ['.csv', 121], '305 - app.py': ['.py', 81], '306 - backend.py': ['.py', 21], '307 - untitled.ui': ['.ui', 217], '308 - untitled_ui.py': ['.py', 97], '309 - settings.json': ['.json', 5], '310 - backend.cpython-314.pyc': ['.pyc', 0], '311 - maxTemp.jpg': ['.jpg', 0], '312 - meanTemp.jpg': ['.jpg', 0], '313 - minTemp.jpg': ['.jpg', 0], '314 - rain.jpg': ['.jpg', 0], '315 - Climate-S006-001(in).csv': ['.csv', 121], '316 - app.py': ['.py', 56], '317 - backend.py': ['.py', 41], '318 - settings.json': ['.json', 5], '319 - backend.cpython-314.pyc': ['.pyc', 0], '320 - index.html': ['.html', 59], '321 - style.css': ['.css', 100], '322 - favicon.ico': ['.ico', 0], '323 - maxTemp.jpg': ['.jpg', 0], '324 - meanTemp.jpg': ['.jpg', 0], '325 - minTemp.jpg': ['.jpg', 0], '326 - rain.jpg': ['.jpg', 0], '327 - Word_Processor___Text_Document_Revision_GCSE_Computer_Science.py': ['.py', 79], '328 - README.md': ['.md', 51], '329 - Correct.mp3': ['.mp3', 0], '330 - Incorrect.mp3': ['.mp3', 0], '331 - SongGuesser.py': ['.py', 553], '332 - Songs.db': ['.db', 0], '333 - Users.db': ['.db', 0], '334 - Aud.mp3': ['.mp3', 0], '335 - Cvr.png': ['.png', 0], '336 - Aud.mp3': ['.mp3', 0], '337 - Cvr.png': ['.png', 0], '338 - Aud.mp3': ['.mp3', 0], '339 - Cvr.png': ['.png', 0], '340 - Aud.mp3': ['.mp3', 0], '341 - Cvr.png': ['.png', 0], '342 - Aud.mp3': ['.mp3', 0], '343 - Cvr.png': ['.png', 0], '344 - untitled.mp3': ['.mp3', 0], '345 - Aud.mp3': ['.mp3', 0], '346 - Cvr.png': ['.png', 0], '347 - Aud.mp3': ['.mp3', 0], '348 - Cvr.png': ['.png', 0], '349 - Aud.mp3': ['.mp3', 0], '350 - Cvr.png': ['.png', 0], '351 - Aud.mp3': ['.mp3', 0], '352 - Cvr.png': ['.png', 0], '353 - Aud.mp3': ['.mp3', 0], '354 - Cvr.png': ['.png', 0], '355 - Aud.mp3': ['.mp3', 0], '356 - Cvr.png': ['.png', 0], '357 - Aud.mp3': ['.mp3', 0], '358 - Cvr.png': ['.png', 0], '359 - Aud.mp3': ['.mp3', 0], '360 - Cvr.png': ['.png', 0], '361 - Aud.mp3': ['.mp3', 0], '362 - Cvr.png': ['.png', 0], '363 - Aud.mp3': ['.mp3', 0], '364 - Cvr.png': ['.png', 0], '365 - Aud.mp3': ['.mp3', 0], '366 - Cvr.png': ['.png', 0], '367 - Aud.mp3': ['.mp3', 0], '368 - Cvr.png': ['.png', 0], '369 - Aud.mp3': ['.mp3', 0], '370 - Cvr.png': ['.png', 0], '371 - Aud.mp3': ['.mp3', 0], '372 - Cvr.png': ['.png', 0], '373 - Aud.mp3': ['.mp3', 0], '374 - Cvr.png': ['.png', 0], '375 - Aud.mp3': ['.mp3', 0], '376 - Cvr.png': ['.png', 0], '377 - Aud.mp3': ['.mp3', 0], '378 - Cvr.png': ['.png', 0], '379 - Aud.mp3': ['.mp3', 0], '380 - Cvr.png': ['.png', 0], '381 - Aud.mp3': ['.mp3', 0], '382 - Cvr.png': ['.png', 0], '383 - Aud.mp3': ['.mp3', 0], '384 - Cvr.png': ['.png', 0], '385 - Aud.mp3': ['.mp3', 0], '386 - Cvr.png': ['.png', 0], '387 - Aud.mp3': ['.mp3', 0], '388 - Cvr.png': ['.png', 0], '389 - Aud.mp3': ['.mp3', 0], '390 - Cvr.png': ['.png', 0], '391 - Aud.mp3': ['.mp3', 0], '392 - Cvr.png': ['.png', 0], '393 - Aud.mp3': ['.mp3', 0], '394 - Cvr.png': ['.png', 0], '395 - Aud.mp3': ['.mp3', 0], '396 - Cvr.png': ['.png', 0], '397 - Aud.mp3': ['.mp3', 0], '398 - Cvr.png': ['.png', 0], '399 - Aud.mp3': ['.mp3', 0], '400 - Cvr.png': ['.png', 0], '401 - Aud.mp3': ['.mp3', 0], '402 - Cvr.png': ['.png', 0], '403 - Aud.mp3': ['.mp3', 0], '404 - Cvr.png': ['.png', 0], '405 - Aud.mp3': ['.mp3', 0], '406 - Cvr.png': ['.png', 0], '407 - Aud.mp3': ['.mp3', 0], '408 - Cvr.png': ['.png', 0], '409 - Aud.mp3': ['.mp3', 0], '410 - Cvr.png': ['.png', 0], '411 - Aud.mp3': ['.mp3', 0], '412 - Cvr.png': ['.png', 0], '413 - Aud.mp3': ['.mp3', 0], '414 - Cvr.png': ['.png', 0], '415 - Aud.mp3': ['.mp3', 0], '416 - Cvr.png': ['.png', 0], '417 - Aud.mp3': ['.mp3', 0], '418 - Cvr.png': ['.png', 0], '419 - README.md': ['.md', 17], '420 - DLC #1.pyproj': ['.pyproj', 35], '421 - DLC__1.py': ['.py', 80], '422 - Songs.db': ['.db', 0], '423 - Aud.mp3': ['.mp3', 0], '424 - Cvr.png': ['.png', 0], '425 - Aud.mp3': ['.mp3', 0], '426 - Cvr.png': ['.png', 0], '427 - Aud.mp3': ['.mp3', 0], '428 - Cvr.png': ['.png', 0], '429 - Aud.mp3': ['.mp3', 0], '430 - Cvr.png': ['.png', 0], '431 - Aud.mp3': ['.mp3', 0], '432 - Cvr.png': ['.png', 0], '433 - Aud.mp3': ['.mp3', 0], '434 - Cvr.png': ['.png', 0], '435 - Aud.mp3': ['.mp3', 0], '436 - Cvr.png': ['.png', 0], '437 - Aud.mp3': ['.mp3', 0], '438 - Cvr.png': ['.png', 0], '439 - Aud.mp3': ['.mp3', 0], '440 - Cvr.png': ['.png', 0], '441 - Aud.mp3': ['.mp3', 0], '442 - Cvr.png': ['.png', 0], '443 - README.md': ['.md', 2], '444 - Mod Loader.py': ['.py', 80], '445 - Songs.db': ['.db', 0]}

        self.__debugging_statement(f"{files = }")
        self.__debugging_statement(f"{len(files) = }")

        file_types = {}

        for file in files:
            if files[file][0] in file_types:
                file_types[files[file][0]] += files[file][1]
            else:
                file_types[files[file][0]] = files[file][1]

        print(f"{file_types = }")

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

                self.__debugging_statement(f"{line_count = }")

                files[f"{file_index} - {file_title}"] = [file_type, line_count]

                file_index += 1

        return files
    
    def __debugging_statement(self, message = ""):
        if self.debugging:
            if message != "":
                print(f"\033[94mDEBUGGING - {message}\033[0m")
            else:
                print()

if __name__ == "__main__":
    app = App(debugging = True)