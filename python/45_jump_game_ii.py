"""
	45. Jump Game II

	Given an array of non-negative integers, you are initially positioned at the first index of the array.

	Each element in the array represents your maximum jump length at that position.

	Your goal is to reach the last index in the minimum number of jumps.

	For example:
		Given array A = [2,3,1,1,4]

	The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        res = [None] * len(nums)

        res[0] = 0

        for i in range(len(nums)):
        	#print res
        	for j in range(1,nums[i]+1):
        		if i + j >= len(nums) -1:
        			return res[i] + 1
        		else:
        			if res[i+j] == None:
        				res[i+j] = res[i] + 1
        			else:
        				res[i+j] = min(res[i+j], res[i] + 1)

        return res[0]
        """
        """
        	Time exceeded.
        """
        step = 0 # steps 
        end = 0 # reache
        curr = 0  # current maximum index can be reached.
        for i in range(len(nums)):
        	if i > end:
        		end = curr
        		step += 1
        	curr = max(curr , i+A[i])
        return step

sol = Solution()
A = [2,3,1,1,4,4]
#A = [25000,24999,24998,24997,24996,24995,24994,24993,24992,24991,24990,24989,24988,24987,24986,24985,24984,24983,24982,24981,24980,24979,24978,24977,24976,24975,24974,24973,24972,24971,24970,24969,24968,24967,24966,24965,24964,24963,24962,24961,24960,24959,24958,24957,24956,24955,24954,24953,24952,24951,24950,24949,24948,24947,24946,24945,24944,24943,24942,24941,24940,24939,24938,24937,24936,24935,24934,24933,24932,24931,24930,24929,24928,24927,24926,24925,24924,24923,24922,24921,24920,24919,24918,24917,24916,24915,24914,24913,24912,24911,24910,24909,24908,24907,24906,24905,24904,24903,24902,24901,24900,24899,24898,24897,24896,24895,24894,24893,24892,24891,24890,24889,24888,24887,24886,24885,24884,24883,24882,24881,24880,24879,24878,24877,24876,24875,24874,24873,24872,24871,24870,24869,24868,24867,24866,24865,24864,24863,24862,24861,24860,24859,24858,24857,24856,24855,24854,24853,24852,24851,24850,24849,24848,24847,24846,24845,24844,24843,24842,24841,24840,24839,24838,24837,24836,24835,24834,24833,24832,24831,24830,24829,24828,24827,24826,24825,24824,24823,24822,24821,24820,24819,24818,24817,24816,24815,24814,24813,24812,24811,24810,24809,24808,24807,24806,24805,24804,24803,24802,24801,24800,24799,24798,24797,24796,24795,24794,24793,24792,24791,24790,24789,24788,24787,24786,24785,24784,24783,24782,24781,24780,24779,24778,24777,24776,24775,24774,24773,24772,24771,24770,24769,24768,24767,24766,24765,24764,24763,24762,24761,24760,24759,24758,24757,24756,24755,24754,24753,24752,24751,24750,24749,24748,24747,24746,24745,24744,24743,24742,24741,24740,24739,24738,24737,24736,24735,24734,24733,24732,24731,24730,24729,24728,24727,24726,24725,24724,24723,24722,24721,24720,24719,24718,24717,24716,24715,24714,24713,24712,24711,24710,24709,24708,24707,24706,24705,24704,24703,24702,24701,24700,24699,24698,24697,24696,24695,24694,24693,24692,24691,24690,24689,24688,24687,24686,24685,24684,24683,24682,24681,24680,24679,24678,24677,24676,24675,24674,24673,24672,24671,24670,24669,24668,24667,24666,24665,24664,24663,24662,24661,24660,24659,24658,24657,24656,24655,24654,24653,24652,24651,24650,24649,24648,24647,24646,24645,24644,24643,24642,24641,24640,24639,24638,24637,24636,24635,24634,24633,24632,24631,24630,24629,24628,24627,24626,24625,24624,24623,24622,24621,24620,24619,24618,24617,24616,24615,24614,24613,24612,24611,24610,24609,24608,24607,24606,24605,24604,24603,24602,24601,24600,24599,24598,24597,24596,24595,24594,24593,24592,24591,24590,24589,24588,24587,24586,24585,24584,24583,24582,24581,24580,24579,24578,24577,24576,24575,24574,24573,24572,24571,24570,24569,24568,24567,24566,24565,24564,24563,24562,24561,24560,24559,24558,24557,24556,24555,24554,24553,24552,24551,24550,24549,24548,24547,24546,24545,24544,24543,24542,24541,24540,24539,24538,24537,24536,24535,24534,24533,24532,24531,24530,24529,24528,24527,24526,24525,24524,24523,24522,24521,24520,24519,24518,24517,24516,24515,24514,24513,24512,24511,24510,24509,24508,24507,24506,24505,24504,24503,24502,24501,24500,24499,24498,24497,24496,24495,24494,24493,24492,24491,24490,24489,24488,24487,24486,24485,24484,24483,24482,24481,24480,24479,24478,24477,24476,24475,24474,24473,24472,24471,24470,24469,24468,24467,24466,24465,24464,24463,24462,24461,24460,24459,24458,24457,24456,24455,24454,24453,24452,24451,24450,24449,24448,24447,24446,24445,24444,24443,24442,24441,24440,24439,24438,24437,24436,24435,24434,24433,24432,24431,24430,24429,24428,24427,24426,24425,24424,24423,24422,24421,24420,24419,24418,24417,24416,24415,24414,24413,24412,24411,24410,24409,24408,24407,24406,24405,24404,24403,24402,24401,24400,24399,24398,24397,24396,24395,24394,24393,24392,24391,24390,24389,24388,24387,24386,24385,24384,24383,24382,24381,24380,24379,24378,24377,24376,24375,24374,24373,24372,24371,24370,24369,24368,24367,24366,24365,24364,24363,24362,24361,24360,24359,24358,24357,24356,24355,24354,24353,24352,24351,24350,24349,24348,24347,24346,24345,24344,24343,24342,24341,24340,24339,24338,24337,24336,24335,24334,24333,24332,24331,24330,24329,24328,24327,24326,24325,24324,24323,24322,24321,24320,24319,24318,24317,24316,24315,24314,24313,24312,24311,24310,24309,24308,24307,24306,24305,24304,24303,24302,24301,24300,24299,24298,24297,24296,24295,24294,24293,24292,24291,24290,24289,24288,24287,24286,24285,24284,24283,24282,24281,24280,24279,24278,24277,24276,24275,24274,24273,24272,24271,24270,24269,24268,24267,24266,24265,24264,24263,24262,24261,24260,24259,24258,24257,24256,24255,24254,24253,24252,24251,24250,24249,24248,24247,24246,24245,24244,24243,24242,24241,24240,24239,24238,24237,24236,24235,24234,24233,24232,24231,24230,24229,24228,24227,24226,24225,24224,24223,24222,24221,24220,24219,24218,24217,24216,24215,24214,24213,24212,24211,24210,24209,24208,24207,24206,24205,24204,24203,24202,24201,24200,24199,24198,24197,24196,24195,24194,24193,24192,24191,24190,24189,24188,24187,24186,24185,24184,24183,24182,24181,24180,24179,24178,24177,24176,24175,24174,24173,24172,24171,24170,24169,24168,24167,24166,24165,24164,24163,24162,24161,24160,24159,24158,24157,24156,24155,24154,24153,24152,24151,24150,24149,24148,24147,24146,24145,24144,24143,24142,24141,24140,24139,24138,24137,24136,24135,24134,24133,24132,24131,24130,24129,24128,24127,24126,24125,24124,24123,24122,24121,24120,24119,24118,24117,24116,24115,24114,24113,24112,24111,24110,24109,24108,24107,24106,24105,24104,24103,24102,24101,24100,24099,24098,24097,24096,24095,24094,24093,24092,24091,24090,24089,24088,24087,24086,24085,24084,24083,24082,24081,24080,24079,24078,24077,24076,24075,24074,24073,24072,24071,24070,24069,24068,24067,24066,24065,24064,24063,24062,24061,24060,24059,24058,24057,24056,24055,24054,24053,24052,24051,24050,24049,24048,24047,24046,24045,24044,24043,24042,24041,24040,24039,24038,24037,24036,24035,24034,24033,24032,24031,24030,24029,24028,24027,24026,24025,24024,24023,24022,24021,24020,24019,24018,24017,24016,24015,24014,24013,24012,24011,24010,24009,24008,24007,24006,24005,24004,24003,24002,24001,24000,23999,23998,23997,23996,23995,23994,23993,23992,23991,23990,23989,23988,23987,23986,23985,23984,23983,23982,23981,23980,23979,23978,23977,23976]
print sol.jump(A)
