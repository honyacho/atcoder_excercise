let puts st = print_string st; print_string "\n";;
let puti num = print_int num; print_string "\n";;
let getSL () = Str.split (Str.regexp " ") (read_line ());;
let getAS () = Array.of_list @@ getSL ();;
let getAI () = Array.of_list @@ List.map int_of_string (getSL ());;
let geti () = int_of_string (read_line ());;
let rep n f =
    let rec repimpl i n = if i < n then (f i; repimpl (i+1) n) else () in repimpl 0 n;;
let rep_from from until f =
    let rec repimpl i n = if i < n then (f i; repimpl (i+1) n) else () in repimpl from until;;


let solve () =
    let len = geti () in
    let inl = getAI () in
    let res = ref 0 in
    rep_from 0 (len-2) (fun i ->
        if (inl.(i) < inl.(i+1) && inl.(i+1) < inl.(i+2)) || (inl.(i+1) < inl.(i) && inl.(i+2) < inl.(i+1)) then
            res := !res + 1
    );
    puti !res;;

solve ();;
