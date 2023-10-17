from pprint import pprint


def upload_music(item, jukebox):
    if item in jukebox:
        print("Musica já existente")
    else:
        jukebox.append(item)
        print(f"Musica {item[0]} adicionada")


def list_genero(genero, jukebox):
    # print(genero)
    if jukebox != []:
        for item in jukebox:
            if item[2] == genero:
                if item[2] != "":
                    print(item[0])
                else:
                    print("Genero desconhecido")
    else:
        print("Sem musicas")


def list_author_musics(author, jukebox):
    print(author)
    if jukebox != []:
        for item in jukebox:
            if item[1] == author:
                if item[0] != "":
                    print(item[0])
                else:
                    print("Autor Sem musicas")
    else:
        print("Sem musicas")


def view_music(key: any, jukebox: any):
    print(key)
    if jukebox != []:
        idx = get_index(key, jukebox)
        if idx is not None:
            print(jukebox[idx][1])
            print(jukebox[idx][2])
            print(jukebox[idx][3])
            print(jukebox[idx][4])
            if jukebox[idx][5] != 0:
                print(f"{key} tocada {jukebox[idx][5]} vezes")
            else:
                print(f"A musica '{key}' nunca foi tocada")
        else:
            print("Musica nao existente")
    else:
        print("Sem musicas")

# Utilizada em várias funções


def get_index(key: any, jukebox: any):
    for item in jukebox:
        if key == item[0]:
            idx = jukebox.index(item)
            if idx >= 0:
                return idx


def delete_music(key, jukebox):
    if jukebox != []:
        idx = get_index(key, jukebox)
        if idx is not None:
            jukebox.remove(jukebox[idx])
        else:
            print(f"Musica {key} nao existe")
    else:
        print("Sem musicas")


def music_freq(playlists_dict: any):
    musicas_em_playlist = []
    frequency = {}
    for item in playlists_dict.items():
        [musicas_em_playlist.append(x) for x in item[1] if not x.isnumeric()]
    for item in musicas_em_playlist:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    musicas_em_playlist_sorted = sorted(
        frequency.items(), key=lambda kv: kv[1], reverse=True)
    print(musicas_em_playlist_sorted)


def get_playlist(var_set):   # var_set = [n, list_name, nmax, tmax, jukebox]
    aux = []
    print(f"Introduzir o nome de {var_set[0]} musicas: ")
    # verifica se a musica existe e adiciona a l_aux
    time = 0
    no_play_list = True
    juke_b = var_set[4]
    for x in range(var_set[0]):
        musica = input(f"{x}> ")
        if musica != "":
            idx = get_index(musica, juke_b)
            if idx is None:
                #print(f"idx2: {idx}")
                print(f"Musica {musica} não existente")
                print("Playlist nao criada")
                no_play_list = False
                aux.clear()
            else:
                # item = juke_b[idx]
                time += int(juke_b[idx][4])
                if time > var_set[3]:
                    print(f"A musica '{juke_b[idx][0]}' excede o tempo")
                    print("Playlist nao criada")
                else:
                    aux.append(musica)
        else:
            print("Dados invalidos")
            no_play_list = False
            break

    if no_play_list:
        aux.append(str(time)) 
        aux.append('0')
        print(f"Playlist '{var_set[1]}' adicionada")
        return {var_set[1]: aux}
    else:
        return {}


def play(key, playlist_dic, jukebox):
    if key in playlist_dic:
        if playlist_dic[key] == []:
            print("Lista vazia")
        else:
            l_trim = playlist_dic[key]
            #print(l_trim)
            l_num = int(l_trim[-1])
            print(l_num)
            l_num += 1
            l_trim[-1] = str(l_num)
            
            playlist_dic[key] = l_trim
            number = len(playlist_dic[key])-2
            l_trim = l_trim[0:number]
            duracao = playlist_dic[key][-2]
            for music in l_trim:
                idx = get_index(music, jukebox)
                l_num = int(jukebox[idx][5])
                l_num += 1
                jukebox[idx][5] = str(l_num)
            print(f"Playlist '{key}' tem {number} musicas e {duracao} segundos")
    else:
        print("key inexistente")


def remove_duplicates(arg: any):
    for key in arg.keys():
        mylist = arg[key]
        mylist = list(dict.fromkeys(mylist))
        arg[key] = mylist


def get_sorted_list(plist):
    local_list = []
    for item in plist.items():    # Create list of all musics in Playlists
        [local_list.append(x) for x in item[1] if not x.isnumeric()]
    frequency = {}  # Sort this list
    for item in local_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    #print(sorted(frequency.items(), key=lambda kv: kv[1], reverse=True))
    return sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)


def list_playlists(arg, plist, juke_b):
    if arg in plist.keys():
        m_list = plist[arg]
        if m_list != []:
            vezes_tocada = m_list[-1]
            total_time = int(m_list[-2])
            m_list = m_list[0: len(m_list)-2]
            for x in m_list:
                idx = get_index(x, juke_b)
                time = int(juke_b[idx][-2])
                print(x, time)
            print(f"Tempo total {total_time}, tocada {vezes_tocada} vezes")
        else:
            print("Playlist vazia")
    else:
        print("Playlist inexistente")


def modify_playlist(arg_1, arg_2, plist_dict, jukebox):  # Edita as Playlists
    nome_plist = input("Nome da Playlist > ")
    # nome_plist = "L4"
    t_time = 0
    if nome_plist in plist_dict:
        m_list = plist_dict[nome_plist]
        if arg_1 == "r":
            if m_list[0] != "":
                t_time = int(m_list[len(m_list)-2])
                if int(arg_2) > len(m_list) - 2 or int(arg_2) <= 0:
                    print("Posicao invalida")
                else:
                    idx = get_index(m_list[int(arg_2)-1], jukebox)
                    time = int(jukebox[idx][-2])
                    t_time = t_time - time
                    print(f"Musica '{m_list[int(arg_2)-1]}' eliminada")
                    del(m_list[int(arg_2)-1])
                    m_list[len(m_list)-2] = str(t_time)
                    plist_dict[nome_plist] = m_list
            else:
                print(f"Lista {nome_plist} vazia")
        else:
            if m_list[0] == "":
                arg_2 = "1"
            if int(arg_2) <= len(m_list) - 1 and int(arg_2) > 0:
                t_time = int(m_list[-2])
                musica = input("Musica a inserir >")
                m_list.insert(int(arg_2)-1, musica)
                time = int(jukebox[get_index(musica, jukebox)][-2])
                t_time = t_time + time
                m_list[len(m_list)-2] = str(t_time)
                plist_dict[nome_plist] = m_list
                print(f"Musica {musica} adicionada")
            else:
                print("Posicao invalida")
    else:
        print("Playlist inexistente")


# Função com uma série de comandos
def music_command(arg, juke_b, p_list: any):
    if arg == "a":
        musicas = []
        total = len(juke_b)
        if juke_b != []:
            [musicas.append(juke_b[x][0]) for x in range(total)]
            for item in musicas:
                if item != "":
                    print(item)
                else:
                    total -= 1
            print(f"Total de musicas {total}")
        else:
            print("Sem musicas")

    elif arg == "i":
        autor = input("Interprete >")
        autores = []
        [autores.append(juke_b[x][1]) for x in range(len(juke_b)) if juke_b[x][1] not in autores]
        if autor in autores:
            list_author_musics(autor, juke_b)
        else:
            print("Autor desconhecido")

    elif arg == "g":
        genero = input("Genero >")
        generos = []
        [generos.append(juke_b[x][2]) for x in range(len(juke_b)) if juke_b[x][2] not in generos]
        if genero in generos:
            list_genero(genero, juke_b)
        else:
            print("Genero desconhecido")

    # Lista as musicas que pertencem a mais do que uma playlist indicando o nº de playlistsmusic em que as musicas entram
    elif arg == "p":
        if juke_b != []:
            m_list = []
            new_dic = p_list
            remove_duplicates(new_dic)
            m_list = get_sorted_list(new_dic)
            # print(m_list)
            num_rep = []
            music_rep = []
            [[num_rep.append(item[1]), music_rep.append(item[0])]
             for item in m_list]
            while len(num_rep) > 0:
                ctl = num_rep.count(num_rep[0])
                for x in range(ctl):
                    print(music_rep[x])
                print(f"Em {num_rep[0]} Playlists")
                if num_rep != []:
                    num_rep = num_rep[ctl:]
                    music_rep = music_rep[ctl:]
        else:
            print("Sem musicas")

    # Lista todas as músicas que pertencem ao top 3 (considera os ex-aquo)
    elif arg == "t":
        if juke_b != []:
            my_dic = dict([(item[0], int(item[5])) for item in juke_b])
            my_dic = dict(
                sorted(my_dic.items(), key=lambda kv: kv[1], reverse=True))
            #print(my_dic)
            tocadas = list(my_dic.values())
            aux_l = []
            # Convert all elements to int
            [aux_l.append(int(x)) for x in tocadas]
            tocadas = aux_l
            musics = list(my_dic.keys())
            loop = 0
            if tocadas[0] != 0:
                while loop <= 2:
                    count = 0
                    max = tocadas[0]
                    if max >= 1:
                        for x in tocadas:
                            if x >= max:
                                count += 1
                        for i in range(count):
                            print(f"{musics[i]} tocada {tocadas[i]} vezes")
                        tocadas = tocadas[count:]
                        musics = musics[count:]
                        loop += 1
                    if tocadas[0] == 0:
                        break
            else:
                print("Nenhuma musica tocada")
        else:
            print("Sem musicas")


def save_data_base(plist, juke_b):
    with open("playlists.txt", 'w') as plist_file, open("jukebox.txt", 'w') as juke_file:
        # Save DATA of Playlists
        for item in plist.items():
            plist_file.write(item[0])  # Name of the Playlist
            plist_file.write("\n")
            # Number of elements in the list
            plist_file.write(str(len(item[1])))
            plist_file.write("\n")
            for x in item[1]:  # Write all elements of the list
                plist_file.write(x)
                plist_file.write("\n")
        # Save DATA of the JUkebox
        for item in juke_b:
            for x in item:
                if x.isdecimal():
                    juke_file.write(str(x))
                    juke_file.write("\n")
                else:
                    juke_file.write(x)
                    juke_file.write("\n")
            juke_file.write("*\n")


def load_data_base(plist, juke_b):
    with open("playlists.txt", 'r') as plist_file, open("jukebox.txt", 'r') as juke_file:
        # Read Playlists
        line = plist_file.readline()
        key = line[: len(line)-1]
        number = int(plist_file.readline())
        while line != '':       # The EOF char is an empty string
            l = []
            for x in range(number):
                line = plist_file.readline()
                if line != "":
                    l.append(line[0: len(line)-1])
                    plist[key] = l
            key = plist_file.readline()
            if key != "":
                key = key[: len(key)-1]
                number = int(plist_file.readline())
        # Read Jukebox
        line = juke_file.readline()
        l = []
        while line != "":
            if line != "*\n":
                l.append(line[0: len(line)-1])
            else:
                juke_b.append(l)
                l = []
            line = juke_file.readline()

 # ******************************** FIM DAS FUNÇÕES *******************************


#
#####################################
# MAIN PROGRAM
###################################


def main():

    # Dados do programa principal

    # Variáveis do programa principal

    #
    jukebox = []

    plist_dict = {}

    flag = True
  # Abre a Jukebox e cria a estrutura Playlist
    while flag:
        comando = input("Nº Máx. de Musicas <spc> Duração Máx : > ")
        if comando.count(" ") == 1:
            nmax = int(comando.split(" ", 2)[0])
            tmax = int(comando.split(" ", 2)[1])
            flag = False
            print("Jukebox aberta")
        else:
            print("Comando invalido")

    comando = "dummy"

    # Recebe o comando, verifica se existem argumentos e separa o comando do argumento
    while comando != "quit":
        comando = input("Comando > ")
        if " " in comando:
            cmd = comando[0: comando.find(" ")]
            arg = comando[comando.find(" ") + 1:]
        else:
            cmd = comando
            arg = ""

        # CREATE
        if cmd == "create":
            if (arg != "") and (arg.isnumeric()) and (int(arg) > 0) and (int(arg) <= nmax):
                name = input("Nome da lista > ")
                if name != "":
                    if name in plist_dict:
                        print(f"Playlist '{name}' já existente")
                    else:
                        var_set = [int(arg), name, nmax, tmax, jukebox]
                        plist_dict.update(get_playlist(var_set))
                        # debug
                        # pprint(plist_dict)
                else:
                    print("Dados invalidos")
            else:
                print("Dados invalidos")
            # debug
            # pprint(plist_dict)
            comando = "dummy"

        # UPLOAD
        elif cmd == "upload":
            item = []
            for x in ["Musica > ", "Autor > ", "Genero > ", "Ano de Lançamento > ", "Duracao >"]:
                entry = input(x)
                item.append(entry)
            item.append("0")
            if item in jukebox:
                print("Musica já existente")
            else:
                jukebox.append(item)
                print(f"Musica {item[0]} adicionada")
            # pprint(jukebox)
            comando = "dummy"

        # PLAY a Playlist
        elif cmd == "play":
            if arg != "":
                play(arg, plist_dict, jukebox)
            else:
                print("Dados invalidos")
            # debug
            # pprint(plist_dict)
            # pprint(jukebox)
            comando = "dummy"

        # DELETE a Music
        elif cmd == "delete":
            if arg != "":
                delete_music(arg, jukebox)
            else:
                print("Dados invalidos")
             # Debug
            # pprint(jukebox)
            comando = "dummy"

        # VIEW a music
        elif cmd == "view":
            if arg != "":
                view_music(arg, jukebox)
            else:
                print("Dados invalidos")

            comando = "dummy"

        # MUSIC + sub_commands
        elif cmd == "music":
            if arg in ["a", "i", "g", "p", "t"]:
                music_command(arg, jukebox, plist_dict)
            else:
                print("Dados invalidos")
            comando = "dummy"

        # PLAYLIST INFO
        elif cmd == "playlist":
            if arg != "":
                if arg in plist_dict:
                    list_playlists(arg, plist_dict, jukebox)
                else:
                    print(f"Lista {arg} inexistente")
            else:
                print("Dados invalidos")
            comando = "dummy"

        # MODIFY Playlist
        elif cmd == "modify":
            arg_1 = arg[0:arg.find(" ")]
            arg_2 = arg[arg.find(" ")+1:]
            if arg_1 != "" and arg_2 != "":
                modify_playlist(arg_1, arg_2, plist_dict, jukebox)
            else:
                arg_2 = comando[-1]
                print("Dados invalidos")
            pprint(plist_dict, width=120)
            comando = "dummy"

        # REMOVE a Playlist
        elif cmd == "remove":
            if arg != "":
                if arg in plist_dict:
                    del(plist_dict[arg])
                else:
                    print(f"Lista {arg} inexistente")
            else:
                print("Dados invalidos")
            comando = "dummy"
        # PRINT DATA BASE
        elif cmd == "see":
            pprint(jukebox, width=120)
            print("\n\n")
            pprint(plist_dict, width=120)
            comando = "dummy"

        # SAVE data_base
        elif cmd == "save":
            save_data_base(plist_dict, jukebox)
            print("DataBase saved")
            comando = "dummy"

        # LOAD data_base
        elif cmd == "load":
            jukebox = []
            load_data_base(plist_dict, jukebox)
            print("DataBase loaded")
            comando = "dummy"
        # QUIT
        
        elif cmd == "quit":
            comando = "quit"
            print("Jukebox encerrada")

        else:
            comando = "dummy"


########
# INICIO DE EXECUÇÃO DO PRGRAMA

main()
