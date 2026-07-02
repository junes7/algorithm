select title, board.board_id, reply_id, reply.writer_id, reply.contents, date_format(reply.created_date,'%Y-%m-%d') as created_date
from used_goods_reply as reply
left join used_goods_board as board
on reply.board_id = board.board_id
where date_format(board.created_date,'%Y-%m') = '2022-10'
order by reply.created_date, title;