world.searchObjects(5, {
    id = world.VolumeType.SPHERE,
    params = {
        point = Airbase.getByName("Larnaca"):getPoint(),
        radius = 3000,
    },
}, function(ot)
    if ot:getTypeName() == 'LARNACA_TERMINAL' then
        ot:destroy()
    end
end)
