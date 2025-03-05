

#Probability of meeting someone at the party
# I assume the probability of meeting someone at a party is proportional to the sum of all edge weights a person has
def prob_meeting(graph, person):
    total_weights=np.sum(graph) 
    person_weights = np.sum(graph[person])
    
    return person_weights/total_weights

# As we meet more people, the connection gets stronger and hence the weight increases by a factor j
def update_weight(graph, a, b, j=0.1):
    if graph[a,b] > 0:
        graph[a,b] += j*(1-graph[a,b])
        graph[b,a]=graph[a,b] # This will keep the symmetry of the edge


def invite(graph, host, threshold = 2000/2215):
    return np.where(graph[host]>threshold)[0]



def attending(invitees, graph, host, base=0.5):
    attendees=[]
    for invitee in invitees:
        friendship_level = graph[host,invitee]
        p_attend = base+0.5*(friendship_level-1500/2215)
        if np.random.rand()<p_attend:
            attendees.append(invitee)
    return np.array(attendees)



def prob_attending(graph,host, invitees):
    return {invitee:0.5+0.5*(graph[host,invitee]-1500/2215) for invitee in invitees}



graph = generate_graph(100, 1 - 2215/4000)
host = 0
invitees = invite(graph, host)
attendees = attending(invitees, graph, host)
probabilities = prob_attending(graph, host, invitees)

print("Invited guests:", invitees)
print("Actual attendees:", attendees)
print("Attendance probabilities:", probabilities)

