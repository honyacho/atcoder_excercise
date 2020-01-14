let puts st = print_endline st
let puti num = print_endline @@ string_of_int num
let getSL () = read_line () |> Str.split (Str.regexp " ")
let getAS () = Array.of_list @@ getSL ()
let getLI () = List.map int_of_string @@ getSL ()
let getAI () = Array.of_list @@ getLI ()
let geti () = int_of_string @@ read_line ()
let rep n f =
    let rec repimpl i n = if i < n then (f i; repimpl (i+1) n) else () in repimpl 0 n
let rep_from from until f =
    let rec repimpl i n = if i < n then (f i; repimpl (i+1) n) else () in repimpl from until