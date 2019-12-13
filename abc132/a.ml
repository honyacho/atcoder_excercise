let puts st = print_string st; print_string "\n";;
let puti num = print_int num; print_string "\n";;
let getSL () = Str.split (Str.regexp " ") (read_line ());;
let getLI () = List.map int_of_string (getSL ());;
let geti () = int_of_string (read_line ());;
let rep n f =
    let rec repimpl i n = if i < n then (f i; repimpl (i+1) n) else () in repimpl 0 n;;
let rep_from from until f =
    let rec repimpl i n = if i < n then (f i; repimpl (i+1) n) else () in repimpl from until;;

module MC = Map.Make(struct
    type t = char
    let compare = compare
end);;

let solve () =
    let str = read_line () in
    let len = String.length str in
    let mp = ref MC.empty in
    rep len (fun i ->
        let ch = (String.get str i) in
        if not @@ MC.mem ch !mp then
            mp := MC.add ch 0 !mp;
        let cnt = MC.find ch !mp in
        mp := MC.add ch (cnt) !mp
    );
    puts @@ if MC.cardinal !mp = 2 then "Yes" else "No";;

solve ();;
