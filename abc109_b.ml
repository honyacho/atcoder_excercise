let puts st = print_string st; print_string "\n";;
let puti num = print_int num; print_string "\n";;
let getSL () = Str.split (Str.regexp " ") (read_line ());;
let getLI () = List.map int_of_string (getSL ());;
let getI () = int_of_string (read_line ());;
let rep n f =
    let rec repimpl i n = if i < n then (f i; repimpl (i+1) n) else () in repimpl 0 n;;
let rep_from from until f =
    let rec repimpl i n = if i < n then (f i; repimpl (i+1) n) else () in repimpl from until;;

let len = getI ();;
let arr = 
    let arr = Array.make len "" in
    rep len (fun i -> arr.(i) <- read_line ());
    arr;;

module SetSt = Set.Make(String);;
let st = ref SetSt.empty

let solve () =
    rep len (fun i -> st := SetSt.add arr.(i) !st);
    if SetSt.cardinal !st = len then begin
        let res = ref true in
        rep (len-1) (fun i -> res := !res && (Str.last_chars arr.(i) 1) = (Str.first_chars arr.(i+1) 1));
        puts @@ if !res then "Yes" else "No";
    end else puts "No";;

solve ();;
