import random

# cgpa, aptitude, interview
# roles (marketing (M), software developer (SD), data analyst (DA))
# rank ((CGPA/10)*0.25 + (Aptitude/100)*0.35 + (INTERVIEW/10)*0.45)

M_MIN_CGPA = 6.7
SD_MIN_CGPA = 7.8
DA_MIN_CGPA = 8.2

m_candidates = []
sd_candidates = []
da_candidates = []
application = 10000

def score(data):
    rank = (data[0]/10)*0.25 + (data[1]/100)*0.3 + (data[2]/10)*0.45
    return round(rank, 2)

def hiring(role):
    if role == 'm': 
        cutoff = M_MIN_CGPA
        l = m_candidates
    elif role == 'sd':
        cutoff = SD_MIN_CGPA
        l = sd_candidates
    elif role == 'da': 
        cutoff = DA_MIN_CGPA
        l = da_candidates

    interviwed_candidates = []
    hired = 0 
    cur_best = 0
    cur_best_candidate = None

    for _ in range(application):
        i = random.randrange(application)
        while(i in interviwed_candidates):
            i = random.randrange(application)
        
        interviwed_candidates.append(i)
        
        if l[i][0] > cutoff:
            s = score(l[i])
            if s > cur_best:
                cur_best = s
                cur_best_candidate = l[i]
                hired += 1

    return hired, cur_best_candidate, cur_best
    

for i in range(application):
    m_candidates.append((random.randint(5, 9) + round(random.random(), 2), random.randint(45, 99), random.randint(3, 9) + round(random.random(), 2)))
    sd_candidates.append((random.randint(5, 9) + round(random.random(), 2), random.randint(45, 99), random.randint(3, 9) + round(random.random(), 2)))
    da_candidates.append((random.randint(5, 9) + round(random.random(), 2), random.randint(45, 99), random.randint(3, 9) + round(random.random(), 2)))

print(f"For Marketing \n\t (Hired, candidate, score) : {hiring('m')}")
print(f"For Software Developer \n\t (Hired, candidate, score) : {hiring('sd')}")
print(f"For Data analyst \n\t (Hired, candidate, score) : {hiring('da')}")