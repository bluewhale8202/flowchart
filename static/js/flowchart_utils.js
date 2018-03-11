function lastOperatorNum(tree){
    var ops = tree.operators;
    var max_num = 0;
    for (id in ops){
        var idx = id.lastIndexOf("_");
        var num = parseInt(id.slice(idx+1));
        if (num > max_num){
            max_num = num;
        }
    }
    return max_num;
}

function rootOperatorIds(tree){
    var ops = tree.operators;
    var links = tree.links;
    var root_check = $.extend({}, ops);
    for (idx in links) {
        delete root_check[links[idx].toOperator];
    }
    return Object.getOwnPropertyNames(root_check);
}


function getOutLinks(tree, cur_op_id){
    var links = tree.links;
    var out_links = [];
    for (idx in links){
        if (links[idx].fromOperator == cur_op_id){
            out_links.push(idx);
        }
    }
    return out_links;
}

function getNextOp(tree, link_id){
    return tree.links[link_id].toOperator;
}
