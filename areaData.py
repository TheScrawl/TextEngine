import npcData

testAreaCentral = {
    
    'name': 'Test Area Central',
    'startText': 'You are in a Test Area',
        
    'npcList': 
        [
            npcData.testNPC,
            npcData.testNPC2,
        ],

    'movement':
        {
            '1':
                {
                    'id': testAreaNorth,
                    'optionText': 'Go north to Test Area North',
                },

            '2':
                {
                    'id': testAreaSouth,
                    'optionText': 'Go south to Test Area South',
                },

            '3':
                {
                    'id': testAreaEast,
                    'optionText': 'Go east to Test Area East',
                },

            '4':
                {
                    'id': testAreaWest,
                    'optionText': 'Go west to test area west',
                },
        }
    }

testAreaNorth = {
    'name': 'Test Area North',
    'startText': 'You are in Test Area North',

    'npcList': None,

    'movement':
        {
            '1':
                {
                    id: testAreaCentral,
                    'optionText': 'Go south to test area central',
                },
        }

    }        

testAreaSouth = {
    'name': 'Test Area South',
    'startText': 'You are in Test Area South',

    'npcList': None,

    'movement':
        {
            '1':
                {
                    'id': testAreaCentral,
                    'optionText': 'Go North to test area central',
                },
        }

    }        

testAreaEast = {
    'name': 'Test Area East',
    'startText': 'You are in Test Area East',

    'npcList': None,

    'movement':
        {
            '1':
                {
                    'id': testAreaCentral,
                    'optionText': 'Go West to test area central',
                },
        }

    }        
    
testAreaWest = {
    'name': 'Test Area West',
    'startText': 'You are in Test Area West',

    'npcList': None,

    'movement':
        {
            '1':
                {
                    'id': testAreaCentral,
                    'optionText': 'Go East to test area central',
                },
        }

    }        
    
