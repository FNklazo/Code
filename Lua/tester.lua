local arr = {'one', 'two', 'three'}

--[[for i=1, #arr do
    print(arr[i])
end


print(table.unpack(arr))

io.write('Type a number (1-3)\n')
local user = io.read()

for i=1, #arr do
    if string.find(arr[i], user) then
        user = arr[i]
        print(user)
        break
    end
end
]]

local s = "hello world from Lua"
for w in string.gmatch(s, "%a+") do
  print(w)
end

